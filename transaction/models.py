from django.db import models


class Transaction(models.Model):
    account = models.ForeignKey(to="account.Account", on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    payee = models.ForeignKey(to="payee.Payee", on_delete=models.PROTECT)
    category = models.ForeignKey(to="category.Category", on_delete=models.PROTECT)
    is_expense = models.BooleanField(default=True)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "transaction"
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
