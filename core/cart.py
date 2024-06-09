from django.http import HttpRequest
from django.conf import settings

from core.models import Course


class Cart:
    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = []

        if not isinstance(cart, list):
            raise ValueError(
                f"{settings.CART_SESSION_ID} should be a list not {type(cart)}"
            )

        if len(cart) > 0:
            valid_courses = Course.objects.filter(id__in=cart).values_list(
                "id", flat=True
            )
            valid_courses = [str(uuid) for uuid in valid_courses]
            prev_cart = cart.copy()
            #
            cart = [course for course in prev_cart if course in valid_courses]
            cart = self.session[settings.CART_SESSION_ID]
            if cart != prev_cart:
                self.session.modified = True

        self.cart = cart

