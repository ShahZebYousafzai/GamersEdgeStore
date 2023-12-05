from .models import GameOrder

def get_user_order(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = GameOrder.objects.get_or_create(customer=user)
        item = order.gameitem_set.all()
        cart_items = order.get_cart_items
        cart_total = order.get_cart_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']
        cart_total = order['get_cart_total']

    return cart_items, cart_total