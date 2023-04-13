from django.shortcuts import render, get_object_or_404
from tvshow.models import Film

#Не полная информация
def film_all_view(request):
    film_list = Film.objects.all()
    context = {
        'film_list': film_list
    }
    return render(request, 'film_list.html', context)

#Подробная информация
def film_detail_view(request, id):
    film_id = get_object_or_404(Film, id=id)
    context = {
        'film_id': film_id
    }
    return render(request, 'film_detail.html', context)