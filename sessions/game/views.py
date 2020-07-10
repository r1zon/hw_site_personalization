from django.shortcuts import render, redirect

from game.models import Player, Game, PlayerGameInfo


def show_home(request):
    template = 'home.html'
    if 'player_id' not in request.session.keys():
        Player.objects.create()
        player = Player.objects.last()
        request.session['player_id'] = player.id
    player = Player.objects.get(id = request.session['player_id'])

    if Game.objects.filter(is_finished = False):
        game = Game.objects.get(is_finished = False)
        if game.creator != request.session['player_id']:
            game.players.add(player.id)
    elif Game.objects.filter(is_finished = True):
        game = Game.objects.get(is_finished=True)
    else:
        Game.objects.create(creator=player.id)
        game = Game.objects.last()
        game.players.add(player.id)
    if PlayerGameInfo.objects.filter(try_counts__gt=0):
        game_info = PlayerGameInfo.objects.get(try_counts__gt=0)
    elif PlayerGameInfo.objects.filter(try_counts=0):
        game_info = PlayerGameInfo.objects.get(player = player.id)
    context = {'game': game,
               'player': player,
               'game_info': game_info
               }
    if game.creator == request.session['player_id']:
        if game.creator == player.id and game.right_answer is None:
            if request.method == 'POST':
                number = request.POST.get('number')
                game.right_answer = number
                game.save()
                return redirect("main_page")
    elif game.creator != request.session['player_id']:
        if player.search_number == game.right_answer:
            game.is_finished = True
            game.save()
        if request.method == 'POST':
            number = request.POST.get('number')
            player.search_number = number
            player.save()
            if player.search_number != game.right_answer:
                print('количество попыток', game_info.try_counts)
                game_info.try_counts += 1
                game_info.save()
            return redirect("main_page")
    return render(
        request,
        'home.html',
        context
    )
