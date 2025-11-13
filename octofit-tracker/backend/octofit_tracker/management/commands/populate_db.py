
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        for model in [Activity, Leaderboard, Workout, User, Team]:
            for obj in model.objects.all():
                if getattr(obj, 'pk', None):
                    obj.delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users (super heroes)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        cap = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)

        # Activities
        Activity.objects.create(user=superman, activity='flight', duration=60)
        Activity.objects.create(user=ironman, activity='run', duration=45)

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=120)
        Leaderboard.objects.create(team=dc, points=110)

        # Workouts
        Workout.objects.create(name='Pushups', difficulty='easy')
        Workout.objects.create(name='Squats', difficulty='medium')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
