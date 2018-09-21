from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from app.models import Character, Book, CoOccur

def home(request):
    return render(request, 'app/home.html', {'title':'Home'})

def about(request):
    return render(request, 'app/about.html', {'title': 'About'})

def all_characters(request):
    character_list = Character.objects.all()
    paginator = Paginator(character_list, 25) 
    page = request.GET.get('page')
    characters = paginator.get_page(page)
    return render(request, 'app/character_list.html', {'title': 'Characters', 'characters':characters})

    
def all_occurrences(request):
    occurrence_list = CoOccur.objects.all()
    paginator = Paginator(occurrence_list, 25) 
    page = request.GET.get('page')
    occurrences = paginator.get_page(page)
    return render(request, 'app/co_occur_list.html', {'title': 'Co-occurrences', 'occurrences':occurrences})


        
