from deals.models import Deal
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def home(request):
    posts = Deal.objects.active()

    return render(request, 'home.html', {"posts": posts})
