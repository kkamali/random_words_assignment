from django.shortcuts import render, HttpResponse, redirect
import random
import string

# Create your views here.
def index(request):
    a_rando = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(14))
    if "attempts" in request.session:
        request.session['attempts'] += 1
    else:
        request.session['attempts'] = 1
    context = {
        "rando" : a_rando,
        "attempts" : request.session['attempts']
    }
    return render(request, "randomwords/index.html", context)

def generate(request):
    return redirect("/")
