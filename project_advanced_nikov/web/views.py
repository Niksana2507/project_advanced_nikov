from django.shortcuts import render

# Create your views here.
def index(request):
    # profile = Profile.objects.first()
    context = {
       # 'profile':profile
    }
    return render(request, "web/index.html", context)

# def nachalo(request):
#     context = {
#
#     }
#     return render(request, "web/index.html", context)