from polls.rest_calls import game
from polls.models import Game, User


def run():
    Game.objects.all().delete()
    game_json=game()
    for e in game_json:
        try:
            user = User.objects.get(username=e['brugernavn'])
        except SomeModel.DoesNotExist:
            user = User.objects.all().first()
        Game.objects.create(
            players=e['spillere'],
            dice=e['terninger'],
            user=user,
            username=e['brugernavn'],
            port=e['port']).save()


