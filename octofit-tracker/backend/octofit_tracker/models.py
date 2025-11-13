from djongo import models

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user.name} - {self.activity}"

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name}: {self.points}"

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name
