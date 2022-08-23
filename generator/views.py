from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'views/home.html')
def about(request):
    return render(request, 'views/about.html')
'''
With this function we're generating password based on conditions that
user selected. 
'''    
def password(request):
    #List of characters with letters of the alphabet
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    # If user selects uppercase checkbox, then
    if(request.GET.get('uppercase')):
        #Add these uppercase characters to the characters list
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # If user selects special characters checkbox, then
    if(request.GET.get('special')):
        #This is not Regex (only special characters) 
        characters.extend(list('!@#$%&*^[]()'))
    #If user selects numbers checkbox, then
    if(request.GET.get('numbers')):
        characters.extend(list('0123456789'))    
    #We go through list and save result of choose values randomly from alphabet list
    #We obtain length of password from page like this:
    for x in range(int(request.GET.get('length'))):
        generated_password += random.choice(characters)
    #Render html view and variable password takes value of generated_password
    return render(request, 'views/password.html', {'password': generated_password})