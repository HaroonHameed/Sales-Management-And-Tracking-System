from django.http import HttpResponse
from django.shortcuts import render
from .models import users
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == 'POST':
        # user = users(request.POST)
        user = request.POST.get('UserName')
        password = request.POST.get('password')
        typeOf = request.POST.get('type')
        # userName = users(request.POST)
        if(typeOf == 'General Manager'):
            return render(request,'GM/index.html',{'userName': user, 'type':typeOf})        
        if(typeOf == 'Sales Force'):
            return render(request,'force/index.html')
        if(typeOf == 'Distributor'):
            return render(request,'distributor/index.html')        
        if(typeOf == 'Area Manager'):
            return render(request,'AreaManager/index.html')    
    return render(request,'login/login.html')
