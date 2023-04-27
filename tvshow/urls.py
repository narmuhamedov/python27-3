from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmListView.as_view(), name='film_list'),
    path('film_list/<int:id>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('add-tvshow/', views.CreateFilmView.as_view(), name='create_film'),
    path('film_delete_or_update_list/', views.DeleteOrUpdateFilmListView.as_view(),
         name='delete_or_update_film_list'),
    path('film_delete/<int:id>/delete/', views.DeleteFilmView.as_view(), name='delete_film_view'),
    path('film_update/<int:id>/update/', views.UpdateFilmView.as_view(), name='update_film_view'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('add-review/', views.ReviewAddView.as_view(), name='add-reviews'),
]








# from tvshow.views import film_all_view, film_detail_view, create_film_view, \
#     delete_film_list_view, film_delete_detail_view, delete_film_view, update_film_view

# urlpatterns = [
#     # path('', film_all_view, name='film_list'),
#     # path('film_list/<int:id>/', film_detail_view, name='film_detail'),
#     # path('add-tvshow/', create_film_view, name='create_film'),
#     # path('film_delete_list/', delete_film_list_view, name='delete_film_list'),
#     # path('film_delete_list/<int:id>/', film_delete_detail_view, name='delete_film_id'),
#     # path('film_delete_list/<int:id>/delete/', delete_film_view, name='delete_film_view'),
#     # path('film_update_list/<int:id>/update/', update_film_view, name='update_film_view'),
# ]