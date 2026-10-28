from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("menu/", views.menu, name="menu"),

    path("cart/", views.cart, name="cart"),

    path("place-order/", views.place_order, name="place_order"),

    path("success/", views.order_success, name="order_success"),

    path("kitchen/", views.kitchen, name="kitchen"),

    path(
        "update-status/<int:order_id>/",
        views.update_order_status,
        name="update_order_status"
    ),

    path(
        "track/<int:order_id>/",
        views.track_order,
        name="track_order"
    ),
]