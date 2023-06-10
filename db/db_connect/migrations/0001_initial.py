# Generated by Django 4.1.9 on 2023-06-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Info",
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
                ("Name", models.CharField(max_length=200)),
                ("Age", models.CharField(max_length=200)),
                ("Phone", models.IntegerField()),
            ],
        ),
    ]
