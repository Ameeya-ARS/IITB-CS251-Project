from django.urls import path

from store.models.review import Review
from .views import home, login, signup, cart, orders, review, product, order_update, edit, vendor_login, vendor_signup, vendor_home, add_product, delete_product, modify_product, modify_form
from .views.login import logout
from .views.vendor_login import vendor_logout
from .views.checkout import Checkout


urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('vendor_home', vendor_home.VendorIndex.as_view(), name='vendor_homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('vendor_signup', vendor_signup.VendorSignup.as_view(), name='vendor_signup'),
    path('edit', edit.Edit.as_view(), name='edit'),
    path('login', login.Login.as_view(), name='login'),
    path('vendor_login', vendor_login.VendorLogin.as_view(), name='vendor_login'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('logout', logout, name='logout'),
    path('vendor_logout', vendor_logout, name='vendor_logout'),
    path('review', review.Reviews.as_view(), name='review'),
    path('product', product.ProductView.as_view(), name='product_page'),
    path('orders', orders.Orders.as_view(), name='orders'),
    path('tracker', order_update.OrderUpdate.as_view(), name='tracker'),
    path('add_product', add_product.AddProduct.as_view(), name='add_product'),
    path('delete_product', delete_product.DeleteProduct.as_view(), name='delete_product'),
    path('modify_product', modify_product.ModifyProduct.as_view(), name='modify product'),
    path('modify_product_form', modify_form.ModifyProductForm.as_view())
]