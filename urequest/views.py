from django.shortcuts import render

# Create your views here.
def requestAuthentication(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        return render(request, 'urequest/requestAuthentication.html', {'username': username, 'password': password})
    else:
        return render(request, 'urequest/requestAuthentication.html')