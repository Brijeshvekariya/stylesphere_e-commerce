from django.shortcuts import render,redirect
from .models import User,Profile,User,Seller,Product
import random,requests

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{"products":products})



def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
            )
            request.session['email']=user.email
            request.session['username']=user.username
            msg = " Login Successfull !"
            return render(request,'index.html',{'msg':msg})
        except:
            try:
                seller = Seller.objects.get(
                        email=request.POST['email'],
                        password=request.POST['password']
                )
                request.session['email'] = seller.email
                request.session['username'] = seller.username
                msg = " Login Successfull ! "
                return render(request,'seller_index.html',{'msg':msg})
            except Exception as e:
                print(e)
                msg1=" Invalid Email or Password !"
                return render(request,'login.html',{'msg1':msg1})
    else:
        return render(request,'login.html')
    

    
def logout(request):
    try:
        del request.session['email']
        del request.session['username']
        return render(request,'login.html')
    except:
        return render(request,'login.html')

def register(request):
    if request.method=="POST":
        try:
            User.objects.get(email = request.POST['email'])
            msg1 = " Email Already Registered ! Please Login"
            return render(request,'login.html',{'msg1':msg1})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password']
                )
                msg = " Account Created Successfully ! "
                return render(request,'login.html',{'msg':msg})
            else:
                msg1 = " Password and Confirm Password does not match ! "
                return render(request,'login.html',{'msg1':msg1})
    else:
        return render(request,'login.html')
    
def seller_register(request):
    if request.method=="POST":
        try:
            Seller.objects.get(email = request.POST['email'])
            msg1 = " Email Already Registered ! Please Login"
            return render(request,'seller_register.html',{'msg1':msg1})
        except:
            if request.POST['password']==request.POST['cpassword']:
                Seller.objects.create(
                    username=request.POST['username'],
                    company = request.POST['company_name'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password']
                )
                msg = " Account Created Successfully ! "
                return render(request,'login.html',{'msg':msg})
            else:
                msg1 = " Password and Confirm Password does not match ! "
                return render(request,'seller_register.html',{'msg1':msg1})
    else:
        return render(request,'seller_register.html')
    
def forgot_password(request):
    if request.method=="POST":
        mobile=request.POST['mobile']
        try:
            user = User.objects.get(mobile=mobile)
            msg = "Hi there! Your one-time password (OTP) for secure access to your e-commerce account is: [OTP]. Please use this code to verify and access your account. Happy shopping!"

            otp = random.randint(1000,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"eYLHjNJ923XdpuOB7gqnTlVPD5FzEUwQ6abGAkR0McrKSIvWimqiMTAY02jxVCHLf8rUQ5BnsJ4PX3Nb",
                           "variables_values":str(otp),
                           "route":"otp",
                           "numbers":user.mobile,
                           "message":"Hi there! Your one-time password (OTP) for secure access to your e-commerce account is: "}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            return render(request,'otp.html',{'otp':otp,'mobile':mobile})
        except:
            msg1=" Mobile Not Registered"
            return render(request,'forgot_password.html',{'msg1':msg1})
    else:
        return render(request,'forgot_password.html')

    
def verify_otp(request):
    if request.method=="POST":
        mobile=request.POST['mobile']
        otp=request.POST['otp']
        uotp=request.POST['uotp']
        if otp==uotp:
            return render(request,'new_password.html',{'mobile':mobile})
        else:
            msg1=" Enter Valid Otp !"
            return render(request,'otp.html',{'msg1':msg1})
    else:
        return render(request,'otp.html')
    
def new_password(request):
    if request.method=="POST":
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if cpassword==password:
                user = User.objects.get(mobile=request.POST['mobile'])
                user.password=password
                user.save()
                msg=" Password Changed Successfully! Login Now."
                return render(request,'login.html',{'msg':msg})
        else:
                msg=" Passwords Do not Match!"
                return render(request,'new_password.html',{'msg':msg})
    else:
        return render(request,'new_password.html')
    
def profile(request):
    user = User.objects.get(email = request.session['email'])
    if request.method=="POST":
        Profile.objects.create(
            user = user,
            address = request.POST['address'],
            city = request.POST['city'],
            state = request.POST['state'],
            country = request.POST['country'],
            pincode = request.POST['pincode'],
            address_type = request.POST['address_type']
        )
        msg = "Address Added Successfully ! "
        return render(request,'profile.html',{'msg':msg})
    else:
        return render(request,'profile.html')

def seller_index(request):
    return render(request,'seller_index.html')


def seller_addproduct(request):
    seller=Seller.objects.get(email=request.session['email'])
    if request.method=="POST":
        Product.objects.create(
            seller=seller,
            product_category=request.POST['product_category'],
            product_subcategory = request.POST['product_subcategory'.title()],
            product_name=request.POST['product_name'.title()],
            product_price=request.POST['product_price'],
            product_discount=request.POST['product_discount'],
            product_desc=request.POST['product_desc'.capitalize()],
            product_image=request.FILES['product_image'],
            product_image_2=request.FILES['product_image_2'],
            product_image_3=request.FILES['product_image_3'],
        )
        msg="Product Added Successfully"
        return render(request,'seller_addproduct.html',{'msg':msg})
    else:
        return render(request,'seller_addproduct.html')
    

def seller_viewproducts(request):
    seller=Seller.objects.get(email = request.session['email'])
    products=Product.objects.filter(seller=seller)
    return render(request,"seller_viewproducts.html",{"products":products,"seller":seller})

def seller_productdetails(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,"seller_productdetails.html", {"product":product})


def seller_editproduct(request,pk):
    seller=Seller.objects.get(email=request.session['email'])
    product=Product.objects.get(pk=pk)
    if request.method=="POST":
        product.product_category=request.POST['product_category'],
        product.product_subcategory = request.POST['product_subcategory'.title()],
        product.product_name=request.POST['product_name'.title()],
        product.product_price=request.POST['product_price'],
        product.product_discount=request.POST['product_discount'],
        product.product_desc=request.POST['product_desc'.capitalize()],
        try:
            product.product_image=request.FILES['product_image'],
            product.product_image_2=request.FILES['product_image_2'],
            product.product_image_3=request.FILES['product_image_3'],
        except:
            pass
        product.save()
        msg="Product Edited Successfully"
        return render(request,'seller_editproduct.html',{'product':product,'msg':msg})
    else:
        return render(request,'seller_editproduct.html',{'product':product})
    
def seller_deleteproduct(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('seller_viewproduct')

def seller_viewmen(request):
     seller=Seller.objects.get(email=request.session['email'])
     products=Product.objects.filter(seller=seller,product_category="Men")
     men = True
     return render(request,'seller_viewproducts.html',{'products':products,"men":men})


def seller_viewwomen(request):
     seller=Seller.objects.get(email=request.session['email'])
     products=Product.objects.filter(seller=seller,product_category="Women")
     women = True
     return render(request,'seller_viewproducts.html',{'products':products,"women":women})


def seller_viewkids(request):
     seller=Seller.objects.get(email=request.session['email'])
     kids = True
     products=Product.objects.filter(seller=seller,product_category="Kids")
     return render(request,'seller_viewproducts.html',{'products':products,"kids":kids})


def product_details(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'product_details.html',{'product':product})

def products(request):
    products = Product.objects.all()
    return render(request,'product.html',{"products":products})

def product_men(request):
    product_men = Product.objects.get(product_category="Men")
    return render(request,'product.html',{"product_men":product_men})