from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, User, Activity, Leaderboard, Workout

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.marvel = Team.objects.create(name='marvel')
        self.dc = Team.objects.create(name='dc')
        self.superman = User.objects.create(name='Superman', email='superman@dc.com', team=self.dc)
        self.ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=self.marvel)
        self.activity = Activity.objects.create(user=self.superman, activity='flight', duration=60)
        self.leaderboard = Leaderboard.objects.create(team=self.marvel, points=120)
        self.workout = Workout.objects.create(name='Pushups', difficulty='easy')

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('teams', response.data)

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activities_endpoint(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts_endpoint(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
