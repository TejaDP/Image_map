from django.shortcuts import render

def king(request):
    return render (request,'main.html')
def queen (request):
    return render (request,'leg.html')
def knight (request):
    return render (request,'lucas.html')
def bishop (request):
    return render (request,'ags.html')
def soldier (request):
    return render (request,'rail.html')
def rook(request):
    return render (request,'icf.html')

