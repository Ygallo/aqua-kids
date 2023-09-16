from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course


def cart_contents(request):

    cart_items = []
    total = 0
    course_count = 0
    cart = request.session.get('cart', {})

    for course_id, quantity in cart.items():
        course = get_object_or_404(Course, pk=course_id)
        total += quantity * course.price
        course_count += quantity
        cart_items.append({
           'item_id': course_id,
           'quantity': quantity,
           'course': course,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'course_count': course_count,
        'grand_total': grand_total,
    }

    return context
