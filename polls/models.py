from polls.rest_calls import create_game, login
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)
    token = models.CharField(max_length=200, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def save(self, force_insert=False, force_update=False, using=None):
        self.token = login(self.username, self.password)
        super(User, self).save()


class Game(models.Model):
    players = models.PositiveIntegerField(
        default=2, validators=[MinValueValidator(2),
                               MaxValueValidator(6)])
    dice = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1),
                               MaxValueValidator(6)])
    port = models.IntegerField(
        default=9000,
        validators=[MinValueValidator(9000),
                    MaxValueValidator(9100)],
        primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " : " + str(self.port)

    def save(self, force_insert=False, force_update=False, using=None):
        if self.username == None or self.username == '':
            self.username = self.user.username
        resp = create_game(self.dice, self.players, self.username, self.user.token)
        super(Game, self).save()

    def remove(self):
        close_game(self.port, self.username, self.token)
        super(Game, self).remove()
