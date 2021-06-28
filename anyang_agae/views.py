from django.shortcuts import render

def main(request):
  return render(request, 'main.html')

def write(request):
  return render(request, 'write.html')