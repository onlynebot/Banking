from django.contrib import admin
from django.urls import path, include
from page.views import (
    HomeView, AboutView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('payment/', include('payment.urls')),



    # Next is to provide the link for the basic pages
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),

]
