from django.shortcuts import render
from .models import QRCode


def index(request):
    if request.method == 'POST':
        name =request.POST.get['name']
        QRCode.objects.create(name=name)
        return redirect('/')

    qrs =QRCode.objects.all().order_by('-id')



    return render(request, 'index.html', {'qrs' : qrs})