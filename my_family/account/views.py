from django.shortcuts import render


def test(request):
    return render(request, "account/test.html", {})


def index(request):
    """
    A basic home page for an account
    """
    return render(request, "account/index.html", {})
