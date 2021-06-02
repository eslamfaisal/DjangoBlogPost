from django.shortcuts import render

# Create your views here.
from account.models import Account


def home_screen_view(request):
    print(request.headers)

    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }

    return render(request, 'personal/home.html', context)
