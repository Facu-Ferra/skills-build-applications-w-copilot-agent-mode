from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
from bson import ObjectId

class Command(BaseCommand):
    help = 'Fix the User model by adding _id as ObjectId in MongoDB directly.'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Update the User collection to add _id field if missing
        users = db.users.find()
        for user in users:
            if '_id' not in user:
                db.users.update_one({'email': user['email']}, {'$set': {'_id': ObjectId()}})

        self.stdout.write(self.style.SUCCESS('Successfully fixed the User model by adding _id field.'))
