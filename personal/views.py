from django.shortcuts import render

# Create your views here.
from personal.models import Question


def home_screen_view(request):
    print(request.headers)

    questions = Question.objects.all()
    context = {
        'questions': questions
    }

    return render(request, 'personal/home.html', context)
