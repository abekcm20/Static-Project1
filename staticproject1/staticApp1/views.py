from django.shortcuts import render

# Create your views here.
def view1(request):
    myname = "Abhishek CM"
    favplayer = "ABD"
    favanimal = "lion"
    favsubject = "Python"
    d = {'name' : myname,'player' : favplayer,'animal' : favanimal,'subject' : favsubject}
    return render(request,'staticApp1/1.html',d)