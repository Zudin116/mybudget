# Generated by Django 4.1.4 on 2022-12-23 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
        ("payee", "0001_initial"),
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trasaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                ("is_expense", models.BooleanField(default=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=15)),
                ("description", models.TextField(blank=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="account.account",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="category.category",
                    ),
                ),
                (
                    "payee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="payee.payee"
                    ),
                ),
            ],
            options={
                "verbose_name": "Transaction",
                "verbose_name_plural": "Transactions",
                "db_table": "transaction",
            },
        ),
    ]
