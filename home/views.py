from django.shortcuts import render
from .models import SpecialOffer


def shop(request):
    return render(request, "shops.html")


def home(request):
    """
    Renders the homepage and displays the latest special offer.

    Retrieves the most recent special offer based on expiry date
    and passes it to the template.

    **Context:**

    `special_offer`
        The latest instance of :model:`SpecialOffer`, or `None`
        if no offers exist.

    **Template:**

    :template:`index.html`
    """
    special_offer = SpecialOffer.objects.order_by('-expiry_date').first()
    return render(request, "home/index.html", {"special_offer": special_offer})
