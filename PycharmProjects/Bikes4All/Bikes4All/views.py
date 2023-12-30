from django.shortcuts import render


def salir(request):
    return render(request, template_name="old_html/logged_out.html")
