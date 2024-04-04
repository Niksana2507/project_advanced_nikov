from django.shortcuts import render

# Create your views here.
def index(request):
    # profile = Profile.objects.first()
    context = {
       # 'profile':profile
    }
    return render(request, "web/index.html", context)

def forus(request):
    # profile = Profile.objects.first()
    context = {
       # 'profile':profile
    }
    return render(request, "web/forus.html", context)

def contact(request):
    # profile = Profile.objects.first()
    context = {
       # 'profile':profile
    }
    return render(request, "web/contact.html", context)

def services(request):
    # profile = Profile.objects.first()
    context = {
       # 'profile':profile
    }
    return render(request, "web/services.html", context)

# def nachalo(request):
#     context = {
#
#     }
#     return render(request, "web/index.html", context)