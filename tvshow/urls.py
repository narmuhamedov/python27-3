from django.urls import path
from tvshow.views import film_all_view, film_detail_view, create_film_view, \
    delete_film_list_view, film_delete_detail_view, delete_film_view, update_film_view

urlpatterns = [
    path('film_list/', film_all_view, name='film_list'),
    path('film_list/<int:id>/', film_detail_view, name='film_detail'),
    path('add-tvshow/', create_film_view, name='create_film'),
    path('film_delete_list/', delete_film_list_view, name='delete_film_list'),
    path('film_delete_list/<int:id>/', film_delete_detail_view, name='delete_film_id'),
    path('film_delete_list/<int:id>/delete/', delete_film_view, name='delete_film_view'),
    path('film_update_list/<int:id>/update/', update_film_view, name='update_film_view'),
]