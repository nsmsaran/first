from django.contrib import admin
from django.urls import path
from triumph import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing),
    path('index',views.index),
    path('todo',views.todo),
    path('articles',views.articles),
    path('journal',views.journal),
    path('articlepage',views.articlepage),
    path('level',views.level),
    path('levelsecond',views.levelsecond),
    path('quiz',views.quiz),
    path('minitube',views.minitube),
    path('podcast',views.podcast)
]
