# django-context-processor-example
This repository has a "before" branch and an "after" branch.<br />
Your goal is to modify the before branch so it becomes the after branch.

## step1
### Create the context processor:
Inside the directory **context-processor-example/demo/demo/** ,<br />
create a file named **context_processor.py** with the following contents:
  ```python
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
  ```

## step2
### Add new context procesor to settings.py:
Inside the **file context-processor-example/demo/demo/settings.py** ,<br />
add **demo.context_processor.template_globals** to the template context_processors:
  ```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["demosite/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'demo.context_processor.template_globals',
            ],
        },
    },
]
  ```
  
## step3
### Remove context variables from views:
Inside the file **context-processor-example/demo/demosite/views.py** ,<br />
remove all the context variables. <br /> 
The **views.py** should look like below when you're done.
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
```

