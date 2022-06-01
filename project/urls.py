
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ecom.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='categorypage'),
    path("product/<int:pk>",product,name='product'),
    path('add-to-cart/',add_cart,name='add-to-cart'),
    path('cart/',show_cart,name='showcart'),
    path('pluscart/',plus_cart),
    path('minuscart/',minus_cart),
    path('removecart/',remove_cart),
    path("logout/",logouts,name='signout'),
    path('paymentdone/',generate_bill,name="generatebill"),
    path('my_bill/',my_bill,name='my_bill'),
    path("all_bill/",all_bill,name="all_bill"),
    path('all_cart/',all_cart,name="all_cart"),
    path("custsignup/", register_request, name='c-signup'),
    path("custsignin/", login_request, name='c-signin'),
    path("addproduct/",Addproduct.as_view(),name="addproduct"),
    path("addcategory/",Addcategory.as_view(),name="addcategory"),
]



urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

