from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "enhancer/index.html")

    def post(self, request, *args, **kwargs):
        if request.FILES:
            url = "https://api.perfectlyclear.io/v1/pfc"
            api_key = "656e43230f7fd759eac3ac55fe4149a2bc0"
            req = requests.put(url, headers={
                "X-API-KEY": api_key,
                "Content-Type": request.FILES['image'].content_type
            }, data=request.FILES['image'].read()
            )
            data = req.json()
            req = requests.get(
                f"https://api.perfectlyclear.io/v1/pfc/{data['imageKey']}", headers={"X-API-KEY": api_key})
            return JsonResponse(req.json())
        print(request.FILES)
        return render(request, "enhancer/index.html")
