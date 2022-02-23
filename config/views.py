from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        return render(request, "today_nsft/main.html")

    def post(self, request):
        return render(request, "today_nsft/main.html")
