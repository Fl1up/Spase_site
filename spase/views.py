from django.shortcuts import render

from spase.models import Spase


# Create your views here.
def main(request):
    spase = Spase.objects.all()

    context = {
        "spase": spase,

    }
    return render(request, "main_list.html", context)