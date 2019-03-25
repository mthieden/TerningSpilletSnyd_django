from polls.rest_calls import game
from polls.models import Game, User


def run():
    Game.objects.all().delete()
    try:
        game_json=game()
        for e in game_json:
            try:
                user = User.objects.get(username=e['brugernavn'])
            except User.DoesNotExist:
                user = User.objects.all().first()
            Game.objects.create(
                players=e['spillere'],
                dice=e['terninger'],
                user=user,
                port=e['port']).save()
    except Exception as e:
        print(e)
        print(dir(e.request))
        return

    print("update succesfull")
    return

