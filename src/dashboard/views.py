from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required()
def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)