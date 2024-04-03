from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("addreviewer", views.add_reviewer, name="revieweradd"),
    # name is used by reverse in url matching and { url } in jinja2 too
    path("invalid", views.invalid, name="invalid"),
    path("thanks", views.thanks, name="thankyou"),
    path('thanks_with_args/<str:first_name>/<str:last_name>/<str:reviewer_email>/',
         views.thanks, name='thanks_with_args'),

]
