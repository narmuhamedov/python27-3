from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from tvshow.models import Film, Reviews
from tvshow.forms import ShowForm, ReviewForm
from django.views import generic
#Не полная информация
class FilmListView(generic.ListView):
    template_name = 'film_list.html'
    queryset = Film.objects.all()

    def get_queryset(self):
        return Film.objects.all()

# def film_all_view(request):
#     film_list = Film.objects.all()
#     context = {
#         'film_list': film_list
#     }
#     return render(request, 'film_list.html', context)

#Подробная информация
class FilmDetailView(generic.DetailView):
    template_name = 'film_detail.html'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(Film, id=film_id)

# def film_detail_view(request, id):
#     film_id = get_object_or_404(Film, id=id)
#     context = {
#         'film_id': film_id
#     }
#     return render(request, 'film_detail.html', context)

#Добавить новый фильм

class CreateFilmView(generic.CreateView):
    template_name = 'crud/create_film.html'
    form_class = ShowForm
    queryset = Film.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateFilmView, self).form_valid(form=form)


# def create_film_view(request):
#     method = request.method
#     if method == "POST":
#         form = ShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Фильм успешно добавлен')
#     else:
#         form = ShowForm()
#     return render(request, 'crud/create_film.html', {'form': form})


#Список фильмов для удаления
class DeleteOrUpdateFilmListView(generic.ListView):
    template_name = 'crud/film_list_delete_or_update.html'
    queryset = Film.objects.all()

    def get_queryset(self):
        return Film.objects.all()
# def delete_film_list_view(request):
#     film_list_delete = Film.objects.all()
#     return render(request, 'crud/film_list_delete_or_update.html', {'film_lst_delete': film_list_delete})
#Список для удаления по id номером
# def film_delete_detail_view(request, id):
#     film_delete_id = get_object_or_404(Film, id=id)
#     return render(request, 'crud/film_delete.html',
#                   {'film_id_delete': film_delete_id})


#Удаление фильма основная логика
class DeleteFilmView(generic.DeleteView):
    template_name = 'crud/film_delete.html'
    success_url = '/film_delete_or_update_list/'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(Film, id=film_id)
# def delete_film_view(request, id):
#     film_id = get_object_or_404(Film, id=id)
#     film_id.delete()
#     return HttpResponse('Фильм успешно удален')


#Изменить фильм
class UpdateFilmView(generic.UpdateView):
    template_name = 'crud/film_update.html'
    form_class = ShowForm
    success_url = '/film_delete_or_update_list/'
    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(Film, id=film_id)


    def form_valid(self, form):
        return super(UpdateFilmView, self).form_valid(form=form)



# def update_film_view(request, id):
#     film_id = get_object_or_404(Film, id=id)
#     if request.method == 'POST':
#         form = ShowForm(instance=film_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Фильм успешно изменен')
#     else:
#         form = ShowForm(instance=film_id)
#
#     context = {
#         'form': form,
#         'film_id': film_id
#     }
#
#     return render(request, 'crud/film_update.html', context)

#Поиск фильмов
class SearchView(generic.ListView):
    template_name = 'film_list.html'
    context_object_name = 'film'
    paginate_by = 5

    def get_queryset(self):
        return Film.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


#Оставить отзыв
class ReviewAddView(generic.CreateView):
    template_name = 'reviews.html'
    form_class = ReviewForm
    queryset = Reviews.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ReviewAddView, self).form_valid(form=form)

