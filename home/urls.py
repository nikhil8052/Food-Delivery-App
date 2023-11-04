from django.urls import path
from home.views import index,get_dish_detail,iniciate_payment,change_payment_status


urlpatterns = [
    path('',index,name='home_page'),
    path('dish/iniciate-payment', iniciate_payment, name='iniciate_payment'),
    path('dish/change-payment-status', change_payment_status, name='change_payment_status'),
    path('dish/<category>/<slug>/<uid>', get_dish_detail, name='get_dish_detail')

]
