from django.urls import path
from .views import AboutPageView, ContactPageView, HomePageView, MenuPageView, IndexPageView

urlpatterns = {
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('menu/', MenuPageView.as_view(), name='menu'),
    path('index/', IndexPageView.as_view(), name='index'),
}
