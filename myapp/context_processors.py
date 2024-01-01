from .models import Product,Cart,Wishlist
def products(request):

    # Retrieve your products here, for example:
    product_subcategory = Product.objects.values('product_subcategory').distinct() # Your product retrieval logic here
    print(product_subcategory)
    cart = Cart.objects.all()

    return {
        'cart':cart,
        'product_subcategory': product_subcategory
    }