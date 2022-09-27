from django.shortcuts import render
from django.http import Http404


from highest_4_biometric.polls.models import Register


def saludo (request):
    try:
        records = Register.objects.all()
    except Register.DoesNotExist:
        raise Http404("Records does not exist")
    return render(request, 'home.html', { 'records': records } )