from django.shortcuts import render

#Home page
def home(request):
    return render(request, 'issue_tracker/home.html')
