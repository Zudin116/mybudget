from django.db import models


class RootCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "root_category"
        verbose_name = "Root category"
        verbose_name_plural = "Root categories"


class Category(models.Model):
    name = models.CharField(max_length=50)
    root_category = models.ForeignKey(to="RootCategory", on_delete=models.PROTECT)
    mounth_expenses_limit = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
