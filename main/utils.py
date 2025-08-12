from main.models import Posts
from django.db.models import Q




def search(query):
    if query.isdigit() and len(query) <= 5:
        return Posts.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 4]
    objects = Q()

    for token in keywords:
        objects |= Q(title__icontains=token)
        objects |= Q(text__icontains=token)

    return Posts.objects.filter(objects)
