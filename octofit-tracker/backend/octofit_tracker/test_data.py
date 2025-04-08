# Test data for OctoFit app

test_users = [
    {"email": "thundergod@mhigh.edu", "name": "Thor", "password": "thundergodpassword"},
    {"email": "metalgeek@mhigh.edu", "name": "Tony Stark", "password": "metalgeekpassword"},
    {"email": "zerocool@mhigh.edu", "name": "Elliot", "password": "zerocoolpassword"},
    {"email": "crashoverride@hmhigh.edu", "name": "Dade", "password": "crashoverridepassword"},
    {"email": "sleeptoken@mhigh.edu", "name": "Sleep Token", "password": "sleeptokenpassword"},
]

test_teams = [
    {"name": "Blue Team", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu"]},
    {"name": "Gold Team", "members": ["zerocool@mhigh.edu", "crashoverride@hmhigh.edu", "sleeptoken@mhigh.edu"]},
]

test_activities = [
    {"user": "thundergod@mhigh.edu", "activity_type": "Cycling", "duration": 60, "date": "2025-04-01"},
    {"user": "metalgeek@mhigh.edu", "activity_type": "Crossfit", "duration": 120, "date": "2025-04-02"},
    {"user": "zerocool@mhigh.edu", "activity_type": "Running", "duration": 90, "date": "2025-04-03"},
    {"user": "crashoverride@hmhigh.edu", "activity_type": "Strength", "duration": 30, "date": "2025-04-04"},
    {"user": "sleeptoken@mhigh.edu", "activity_type": "Swimming", "duration": 75, "date": "2025-04-05"},
]

test_leaderboard = [
    {"team": "Blue Team", "points": 200},
    {"team": "Gold Team", "points": 250},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event", "duration": 60},
    {"name": "Crossfit", "description": "Training for a crossfit competition", "duration": 120},
    {"name": "Running Training", "description": "Training for a marathon", "duration": 90},
    {"name": "Strength Training", "description": "Training for strength", "duration": 30},
    {"name": "Swimming Training", "description": "Training for a swimming competition", "duration": 75},
]
