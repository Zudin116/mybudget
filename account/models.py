from django.db import models
from decimal import *


class Account(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    def balance(self) -> Decimal:
        return Decimal(15.5)

    class Meta:
        db_table = "account"
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
