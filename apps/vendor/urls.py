from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<slug:product_slug>/', views.edit_product, name='edit_product'),
    path('delete-product/<slug:product_slug>/', views.delete_product, name='delete_product'),
    path('orders/', views.vendor_orders, name='vendor_orders'),
    path('order/edit/<int:order_id>/', views.vendor_order_edit, name='vendor_order_edit'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
]