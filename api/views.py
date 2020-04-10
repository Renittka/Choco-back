from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from api.models import Category, Restaurant, Product
from django.http import JsonResponse


@csrf_exempt
def categories_list(request):
    pass


@csrf_exempt
def category_restaurants(request):
    pass


@csrf_exempt
def restaurants_products(request):
    pass


@csrf_exempt
def product_order(request):
    pass


@csrf_exempt
def login(request):
    pass


@csrf_exempt
def signup(request):
    pass


