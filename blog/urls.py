from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("<int:pk>", views.current, name="current"),
]
