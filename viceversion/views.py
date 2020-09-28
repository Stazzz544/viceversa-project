from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	words = (user_text.count(" "))+1
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html' , {'words':words, 'usertext':user_text, 'reversetext':reversed_text})
