from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'landing.html')
def index(request):
    return render(request,'index.html')
def todo(request):
    return render(request,'todo.html')
def articles(request):
    return render(request,'articles.html')
def journal(request):
    return render(request,'journal.html')
def articlepage(request):
    return render(request,'articlepage.html')
def level(request):
    return render(request,'level.html') 
def levelsecond(request):
    return render(request,'levelsecond.html')
def quiz(request):
    return render(request,'quiz.html')
def minitube(request):
    return render(request,'minitube.html')
def podcast(request):
    return render(request,'podcast.html') 
