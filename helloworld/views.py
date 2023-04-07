from django.shortcuts import render
import random
# Create your views here.


def indexPageView(request):

    languages = ["Python", "C#", "JavaScript", "Swift", "Java"]
    context = {
        "data": random.choice(languages)
    }
    return render(request, "index.html", context)
