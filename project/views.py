from django.shortcuts import redirect, render


def get_404_er(request, exception):

    return render(request, './mumber_/404.html', status=404)
    