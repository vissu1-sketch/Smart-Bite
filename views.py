import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Order


# Home Page
def home(request):
    return render(request, "restaurant/home.html")


# Menu Page
def menu(request):
    table_number = request.GET.get("table", 1)

    return render(
        request,
        "restaurant/menu.html",
        {
            "table_number": table_number
        }
    )


# Cart Page
def cart(request):
    return render(request, "restaurant/cart.html")


# Place Order
@csrf_exempt
def place_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            table_number = data.get("table_number", 1)
            customer_name = data.get("customer_name", "")
            items = data.get("items", "[]")
            total_amount = data.get("total_amount", 0)

            order = Order.objects.create(
                table_number=table_number,
                customer_name=customer_name,
                items=items,
                total_amount=total_amount,
                status="Pending"
            )

            return JsonResponse({
                "success": True,
                "order_id": order.order_id
            })

        except Exception as error:
            return JsonResponse({
                "success": False,
                "message": str(error)
            }, status=400)

    return JsonResponse({
        "success": False,
        "message": "Only POST requests are allowed"
    }, status=405)


# Order Success Page
def order_success(request):
    order_id = request.GET.get("order")

    order = None

    if order_id:
        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            order = None

    return render(
        request,
        "restaurant/success.html",
        {
            "order": order
        }
    )


# Kitchen Dashboard

def kitchen(request):
    orders = Order.objects.all().order_by("-created_at")

    for order in orders:
        try:
            order.display_items = json.loads(order.items)
            if not isinstance(order.display_items, list):
                order.display_items = []
        except (json.JSONDecodeError, TypeError):
            order.display_items = []

    return render(
        request,
        "restaurant/kitchen.html",
        {"orders": orders}
    )



# Update Order Status
@csrf_exempt
def update_order_status(request, order_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            new_status = data.get("status")

            allowed_statuses = [
                "Pending",
                "Preparing",
                "Ready"
            ]

            if new_status not in allowed_statuses:
                return JsonResponse({
                    "success": False,
                    "message": "Invalid status"
                }, status=400)

            order = Order.objects.get(order_id=order_id)

            order.status = new_status
            order.save()

            return JsonResponse({
                "success": True,
                "status": order.status
            })

        except Order.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Order not found"
            }, status=404)

        except Exception as error:
            return JsonResponse({
                "success": False,
                "message": str(error)
            }, status=400)

    return JsonResponse({
        "success": False,
        "message": "Only POST requests are allowed"
    }, status=405)


# Customer Order Tracking
def track_order(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)

        return render(
            request,
            "restaurant/track.html",
            {
                "order": order
            }
        )

    except Order.DoesNotExist:
        return render(
            request,
            "restaurant/not_found.html"
        )