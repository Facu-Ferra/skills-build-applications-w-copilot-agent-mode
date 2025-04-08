from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
from bson import ObjectId

class Command(BaseCommand):
    help = 'Perform manual migration to fix schema issues with djongo.'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Add _id field to User collection if missing
        users = db.users.find()
        for user in users:
            if '_id' not in user:
                db.users.update_one({'email': user['email']}, {'$set': {'_id': ObjectId()}})

        # Create TeamMember collection for ManyToMany relationship
        if 'teammember' not in db.list_collection_names():
            db.create_collection('teammember')

        self.stdout.write(self.style.SUCCESS('Manual migration completed successfully.'))
