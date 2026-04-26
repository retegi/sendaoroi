from django.shortcuts import render

from applications.faq.models import FAQ
from .models import HomeContent


def home(request):
    content = HomeContent.get_active()
    home_faqs = FAQ.objects.filter(is_active=True, show_on_home=True).order_by("order", "id")[:5]
    return render(
        request,
        "home/index.html",
        {
            "home_content": content,
            "home_faqs": home_faqs,
        },
    )
