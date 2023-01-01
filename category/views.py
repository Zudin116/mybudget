from django.shortcuts import render
from account.models import Account


def index(request):
    context = {
        "accounts": Account.objects.all(),
    }
    return render(request, "category/index.html", context)
