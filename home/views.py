from django.shortcuts import render,redirect,reverse
from dishes.models import Dish
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import razorpay
from django.conf import settings 
from .models import Order
from django.http import JsonResponse

def index(request):
    dishes=Dish.objects.all()

    return render(request,'home/index.html',{"dishes":dishes})

def get_dish_detail(request, category, slug, uid ):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')

    dish=Dish.objects.get(uid=uid)
    return render(request,'home/dish_detail.html',{"dish":dish})



def iniciate_payment(request):

    if not request.user.is_authenticated:
        response={
            'status':500,
            'message':'Authentication Failed'
        }
        return JsonResponse(response)
    
    client=razorpay.Client(auth=(settings.KEY, settings.SECRET))
    params={
        'amount':'5000',
        'currency':'INR',
        'payment_capture':True
    }
    payment=client.order.create(params)
    Order.objects.create(user=request.user,order_id=payment['id'], amount=100,payment_status="Iniciated")
    response={
        'status':200,
        'data':payment
    }
    return JsonResponse(response)



def change_payment_status(request):
    Order.objects.create(order_id=request.order_id,payment_id=request.payment_id,payment_status=request.payment_status)
