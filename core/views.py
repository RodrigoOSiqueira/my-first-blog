from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
	template_name='core/home.html'
	return render(request,template_name)