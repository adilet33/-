from django.shortcuts import render
from .models import Graduate


def graduate_list(request):
    graduates = Graduate.objects.all()
    return render(request, 'graduates/gradueate_list.html', {'graduates': graduates})



def graduate_detail(request, graduate_id):
    graduate = get_object_or_404(Graduate, pk=graduate_id)
    return render(request, 'graduates/graduate_detail.html', {'graduate': graduate})



