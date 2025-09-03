

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),  # from earlier
    path('', views.dashboard, name='dashboard'),

    path('member/add/', views.add_member, name='add_member'),
    path('member/update/<int:pk>/', views.update_member, name='update_member'),
    path('member/delete/<int:pk>/', views.delete_member, name='delete_member'),
    path('trader/add/', views.add_trader, name='add_trader'),
    path('trader/update/<int:pk>/', views.update_trader, name='update_trader'),
    path('trader/delete/<int:pk>/', views.delete_trader, name='delete_trader'),
    path('member/view/<int:pk>/', views.view_member, name='view_member'),
   path('trader/view/<int:pk>/', views.view_trader, name='view_trader'),

   # Financial Reports CRUD
path('financial/add/', views.add_financial_report, name='add_financial_report'),
path('financial/view/<int:pk>/', views.view_financial_report, name='view_financial_report'),
path('financial/update/<int:pk>/', views.update_financial_report, name='update_financial_report'),
path('financial/delete/<int:pk>/', views.delete_financial_report, name='delete_financial_report'),
]