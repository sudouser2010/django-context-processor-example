from django.template import RequestContext
def template_globals(request):
    return {
        "COMPANY_NAME": "EAT AT JOE'S",
        "PHONE_NUMBER": "555-555-5555",
        "STREET_ADDRESS": "555 NW 2000 Brick RD",
        "CITY": "Wala Wala",
        "STATE": "Vermont",
        "COMPANY_SERVICE": "eat pizza",
    }