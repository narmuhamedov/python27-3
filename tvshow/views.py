from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from tvshow.models import Film
from tvshow.forms import ShowForm
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

#Добавить новый фильм
def create_film_view(request):
    method = request.method
    if method == "POST":
        form = ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Фильм успешно добавлен')
    else:
        form = ShowForm()
    return render(request, 'crud/create_film.html', {'form': form})


#Список фильмов для удаления
def delete_film_list_view(request):
    film_list_delete = Film.objects.all()
    return render(request, 'crud/film_list_delete_or_update.html', {'film_lst_delete': film_list_delete})
#Список для удаления по id номером
def film_delete_detail_view(request, id):
    film_delete_id = get_object_or_404(Film, id=id)
    return render(request, 'crud/film_id_delete_or_update.html',
                  {'film_id_delete': film_delete_id})


#Удаление фильма основная логика
def delete_film_view(request, id):
    film_id = get_object_or_404(Film, id=id)
    film_id.delete()
    return HttpResponse('Фильм успешно удален')


#Изменить фильм
def update_film_view(request, id):
    film_id = get_object_or_404(Film, id=id)
    if request.method == 'POST':
        form = ShowForm(instance=film_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Фильм успешно изменен')
    else:
        form = ShowForm(instance=film_id)

    context = {
        'form': form,
        'film_id': film_id
    }

    return render(request, 'crud/film_update.html', context)