from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout, TeamMember
from datetime import date
from django.db import transaction
from bson import ObjectId
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')
        
        with transaction.atomic():
            # Save all teams to ensure they have primary keys before clearing members
            for team in Team.objects.all():
                team.save()

            # Debugging each step
            self.stdout.write('Clearing existing data...')
            User.objects.all().delete()
            # Removed Django ORM deletion for Team objects
            # Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            # Ensure ObjectId is used correctly for relationships
            self.stdout.write('Creating users...')
            users = [
                User(_id="0001", email='user1@example.com', name='User One', password='password1'),
                User(_id="0002", email='user2@example.com', name='User Two', password='password2'),
                User(_id="0003", email='user3@example.com', name='User Three', password='password3'),
            ]
            User.objects.bulk_create(users)

            # Ensure all Team objects are saved before performing operations
            # Use MongoDB operations to clear the Team collection
            client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
            db = client[settings.DATABASES['default']['NAME']]
            db.teams.delete_many({})

            self.stdout.write('Creating teams...')
            team1 = Team(name='Team Alpha')
            team1.save()

            team2 = Team(name='Team Beta')
            team2.save()

            # Use MongoDB operations for TeamMember relationships
            client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
            db = client[settings.DATABASES['default']['NAME']]

            # Create TeamMember relationships directly in MongoDB
            db.teammember.insert_many([
                {"team_id": team1.id, "user_id": str(users[0]._id)},
                {"team_id": team1.id, "user_id": str(users[1]._id)},
                {"team_id": team2.id, "user_id": str(users[1]._id)},
                {"team_id": team2.id, "user_id": str(users[2]._id)},
            ])

            self.stdout.write('Creating activities...')
            # Create activities
            activities = [
                Activity(user=users[0], activity_type='Running', duration=30, date=date(2025, 4, 1)),
                Activity(user=users[1], activity_type='Cycling', duration=45, date=date(2025, 4, 2)),
                Activity(user=users[2], activity_type='Swimming', duration=60, date=date(2025, 4, 3)),
            ]
            Activity.objects.bulk_create(activities)

            self.stdout.write('Creating leaderboard entries...')
            # Corrected the `team` field in Leaderboard to reference the `id` field of Team
            leaderboard_entries = [
                Leaderboard(team=team1, points=100),
                Leaderboard(team=team2, points=150),
            ]
            Leaderboard.objects.bulk_create(leaderboard_entries)

            self.stdout.write('Creating workouts...')
            # Create workouts
            workouts = [
                Workout(name='Morning Run', description='A quick morning run', duration=30),
                Workout(name='Evening Yoga', description='Relaxing yoga session', duration=60),
            ]
            Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Database population completed successfully.'))
