from django.shortcuts import render


# Create your views here.
def home_screen_view(request):
    print(request.headers)

    context = {
        'some_string': 'this is some string that i passing to he view'
    }

    return render(request, 'personal/home.html', context)
