from django.shortcuts import render
from django.http import JsonResponse
from .gains_calculator import calculate
import json

def index(request):
    return render(request, "index.html")

def compute(request):

    if request.method == "POST":

        # TODO put into a django form
        data = json.loads(request.body)
        current_age = int(data["current_age"])
        retire_age = int(data["retire_age"])
        current_amount = float(data["current_amount"])
        interest_rate = float(data["interest_rate"])
        savings_result = calculate(current_age, retire_age, current_amount, interest_rate)
        stock_market_result = calculate(current_age, retire_age, current_amount)
        difference = stock_market_result - savings_result


        return JsonResponse({
            "savings_result": savings_result,
            "stock_market_result": stock_market_result,
            "difference": difference
         })
    else:
        return JsonResponse({})
