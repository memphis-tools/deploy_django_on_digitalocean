from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "ADMIN"
    USER = "USER"
    ROLES_SET = (
        (ADMIN, "administrateur"),
        (USER, "utilisateur"),
    )
    role = models.CharField(max_length=15, choices=ROLES_SET, default=ROLES_SET[1][0], verbose_name="role")

    def __str__(self):
        return f"{self.username}"
