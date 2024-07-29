from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse('am the first page to be rendered')

def help(request):
  my_dict = { 'insert_me': "am from the template side"}
  return render(request, 'myapp/help.html', context=my_dict)