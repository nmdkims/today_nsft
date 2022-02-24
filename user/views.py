import os
from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.views import APIView

from config.settings import MEDIA_ROOT
from user.models import User


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            thumbnail="default_profile.jpg")

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))

        if user.check_password(password):
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))


class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, 'user/login.html')


class UpdateProfile(APIView):
    def post(self, request):
        email = request.session.get('email', None)
        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, 'user/login.html')

        file = request.FILES['file']
        if file is None:
            return Response(status=500)

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        user.thumbnail = uuid_name
        user.save()

        return Response(status=200, data=dict(uuid=uuid_name))