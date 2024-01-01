from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField(max_length=30, unique=True)
    mobile = models.PositiveIntegerField( unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username

class Seller(models.Model):
    username = models.CharField(max_length=10,unique=True)
    company = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    mobile = models.PositiveIntegerField(unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pincode = models.PositiveIntegerField()
    choice = (
        ("Residence","Residence"),
        ("Office","Office"),
    )
    address_type = models.CharField(max_length=20,choices=choice)

    def __str__(self) :
        return self.user.username
    
class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    choice1 = (
        ("Mens","Mens"),
        ("Women","Women"),
        ("Kids","Kids")
    )
    product_category = models.CharField(max_length=50,choices=choice1)
    product_subcategory = models.CharField(max_length=50)
    product_name=models.CharField(max_length=100)
    product_price=models.PositiveIntegerField()
    product_discount=models.PositiveIntegerField()
    product_desc=models.TextField()
    product_image=models.ImageField(upload_to="product_name",default=True)
    product_image_2=models.ImageField(upload_to="product_name2",default=True)
    product_image_3=models.ImageField(upload_to="product_name3",default=True)

    def __str__(self):
        return self.product_category+" "+self.product_subcategory+" "+self.product_name
    
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username+" - "+self.product.product_name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_price=models.PositiveIntegerField()
    product_qty=models.PositiveIntegerField(default=1)
    total_price=models.PositiveIntegerField()
    payment_status=models.BooleanField(default=False)

    def __str__(self):
           return self.user.username+" - "+self.product.product_name