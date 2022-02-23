from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    """
         프로필 사진 저장
         닉네임 -> 화면에 표기되는 이름
         이메일 주소 -> 회원가입할때 사용하는 아이디
         비밀번호
    """
    profile_image = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "User"
