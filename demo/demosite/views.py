from django.shortcuts import render

def home(request):
    context = {
        "COMPANY_NAME": "EAT AT JOE'S",
        "PHONE_NUMBER": "555-555-5555",
        "COMPANY_SERVICE": "eat pizza",
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        "COMPANY_NAME": "EAT AT JOE'S",
        "PHONE_NUMBER": "555-555-5555",
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "COMPANY_NAME": "EAT AT JOE'S",
        "PHONE_NUMBER": "555-555-5555",
        "STREET_ADDRESS": "555 NW 2000 Brick RD",
        "CITY": "Wala Wala",
        "STATE": "Vermont"
    }
    return render(request, 'contact.html', context)