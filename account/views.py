from . import models
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("paging:index")

        messages.error(request, "Invalid credentials")
        return redirect(request.GET.get("next", "account:login"))
    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("account:login")

        for i, j in form.errors.items():
            messages.error(request, f"{i}: {j[0]}")
        return redirect("account:register")
    return render(request, "account/register.html")


def logout_view(request):
    auth.logout(request)
    return redirect("paging:index")
    # return redirect(request.META.get("HTTP_REFERER", "account:login"))


def subscribe_view(request):
    if request.method != "POST":
        messages.warning(request, "you can only subscribe here")
        return redirect(request.META.get("HTTP_REFERER", "paging:index"))

    email = request.POST.get("email")
    is_present = models.Subscribtion.objects.filter(email=email).exists()
    if is_present:
        messages.info(request, "you have already subscribed")
    else:
        models.Subscribtion.objects.create(email=email)
        messages.success(request, "you are now a registered subscriber, stay tuned")

    return redirect(request.META.get("HTTP_REFERER", "paging:index"))
