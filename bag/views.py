from django.shortcuts import redirect, get_object_or_404
from products.models import Product


def add_to_bag(request, product_id):
    """
    Add a product to the shopping bag.
    Stores quantity and configuration (license/print type).
    """
    product = get_object_or_404(Product, pk=product_id)

    quantity = int(request.POST.get('quantity'))
    product_format = request.POST.get('format')
    license_id = request.POST.get('license')
    print_type = request.POST.get('print_type')

    bag = request.session.get('bag', {})

    item_key = f"{product_id}-{product_format}"
    if product_format == 'digital' and license_id:
        item_key += f"-{license_id}"
    elif product_format == 'printed' and print_type:
        item_key += f"-{print_type}"

    if item_key in bag:
        bag[item_key]['quantity'] += quantity
    else:
        bag[item_key] = {
            'product_id': product_id,
            'format': product_format,
            'license': license_id,
            'print_type': print_type,
            'quantity': quantity,
        }

    request.session['bag'] = bag
    return redirect('view_bag')
