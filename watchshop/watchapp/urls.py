from django.contrib import admin
from django.urls import path
from .views import Home,Upload,login_user,logout_user,signup_user,show_product,addtowish,show_list,removewish,addtocart,show_cart,removecart
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', Home ,name='home'),
   path('upload',Upload ,name='upload'),
   path('login', login_user, name='login'),
   path('signup', signup_user, name='signup'),
   path('logout', logout_user, name='logout'),
   path('product/<int:id>', show_product, name='product'),
   path('addtowish/<int:id>',addtowish, name='addtowish'),
   path('addtocart/<int:id>',addtocart,name='addtocart'),
   path('wishlist',show_list,name='show_list'),
   path('cart',show_cart,name='show_cart'),
   path('removewish<int:id>',removewish, name='removewish'),
   path('removecart<int:id>',removecart, name='removecart'),
 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)