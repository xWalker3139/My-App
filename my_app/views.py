from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.views.generic import View
from django.http import Http404

class BaseView(View):
    def get(self, request):
        return render(request, "my_app/base.html")

class ContactView(View):
    def get(self, request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                return render(request, "my_app/contact.html")
            else:
                return Http404
        return render(request, "my_app/contact.html")

# Create your views here.
