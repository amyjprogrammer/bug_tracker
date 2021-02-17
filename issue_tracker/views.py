from django.shortcuts import render

#Home page will show all the open tickets (no login required)
def home(request):
    return render(request, 'issue_tracker/home.html')
