from .models import Product
def products(request):

    # Retrieve your products here, for example:
    product_subcategory = Product.objects.values('product_subcategory').distinct() # Your product retrieval logic here
    print(product_subcategory)

    return {
        'product_subcategory': product_subcategory
    }