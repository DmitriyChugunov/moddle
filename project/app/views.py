from django.shortcuts import render

PostList = [
    {'id': 1, 'name': 'Открытие школы', 'text': 'В городе Елабуга была открыта новая общеобразовательная школа',
     'image': '/static/skoll.jpg', 'comment': 'Очень круто!', 'like': 8},
    {'id': 2, 'name': 'Новый завод Алабуги',
     'text': 'В городе Елабуга был построен новый завод по производству студентов "Роботов"',
     'image': '/static/zavod.jpg', 'comment': 'Очень интересно!', 'like': 10}
]


def PostIdView(request, id):
    post = {}
    for i in PostList:
        if i['id'] == int(id):
            post = i
            break
    return render(request, 'post.html', {'post': post})


def PostView(request):
    return render(request, 'posts.html', context={'form': PostList})
