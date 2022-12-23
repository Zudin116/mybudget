from django.db import models


class Payee(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "payee"
        verbose_name = "Payee"
        verbose_name_plural = "Payees"
