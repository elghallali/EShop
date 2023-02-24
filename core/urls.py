from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

anonymous_required = user_passes_test(lambda user: not user.is_authenticated, login_url='/')

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.ContactUsView.as_view(), name='contact'),
    path('about/', views.aboutUs, name='about'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('shop/', views.shop, name='shop'),

    path('add-address/', views.ProfileView.as_view(), name='add-address'),
    path('addresses/', views.address, name='addresses'),
    path('update-address/<int:pk>', views.UpdateAddress.as_view(), name='update-address'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show-cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('plus-cart/', views.plus_cart),
    path('minus-cart/', views.minus_cart),
    path('remove-cart/', views.remove_cart),


    # Login authentication
    path('customer-registration/', anonymous_required(views.CustomerRegistrationView.as_view()), name='customer-registration'),
    path('accounts/login/', anonymous_required(auth_view.LoginView.as_view(template_name='login.html', authentication_form =LoginForm)), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='home'), name='logout'),

    # Reset Password
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password/password-reset.html', form_class =MyPasswordResetForm), name='password-reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password/password-reset-done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='password/password-reset-confirm.html', form_class =MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete', auth_view.PasswordResetCompleteView.as_view(template_name='password/password-reset-complete.html'), name='password_reset_complete'),

    # Change Password
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='password/password-change.html', form_class =MyPasswordChangeForm, success_url="/password-change-done"), name='password-change'),
    path('password-change-done/', auth_view.PasswordChangeDoneView.as_view(template_name='password/password-change-done.html'), name='password-change-done'),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)