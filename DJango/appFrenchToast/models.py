from django.db import models

# Create your models here.

class User(models.Model):
	user_ID = models.IntegerField(primary_key=True, unique=True)
	username = models.CharField(max_length=32, null=False, unique=True)
	password = models.CharField(max_length=20, null=False, unique=True)
	email = models.CharField(max_length=32, null=False)

	
class Game(models.Model):
	game_ID = models.IntegerField(primary_key=True, unique=True)
	owning_user = models.ForeignKey(User)
	answer = models.CharField(max_length=20, null=False)
	date = models.DateField(null=False)
	
class Moves(models.Model):
	game = models.ForeignKey(Game, null=False)
	guessA = models.CharField(max_length=32, null=False)
	scoreA = models.IntegerField()
	guessB = models.CharField(max_length=32, null=False)
	scoreB = models.IntegerField()
	responseChoices = (
		('A', 'First'),
		('B', 'Second'),
	)
	response = models.CharField(max_length=1, choices=responseChoices)