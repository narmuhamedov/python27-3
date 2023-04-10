from django.urls import path
from blog.views import helloview, blogview

urlpatterns = [
    path('hello/', helloview, name='hello'),
    path('post/', blogview, name='post'),
]