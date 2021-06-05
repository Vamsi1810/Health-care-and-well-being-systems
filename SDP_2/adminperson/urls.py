from django.urls import path

from . import views

urlpatterns =[
    path('',views.AdminHomePage,name="adminhome"),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    # path('chart', line_chart, name='line_chart'),
    # path('chartJSON', line_chart_json, name='line_chart_json'),
]