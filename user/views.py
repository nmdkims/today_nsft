from django.shortcuts import render
from rest_framework.views import APIView


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

