# Generated by Django 5.0.6 on 2024-06-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "member_id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("member_password", models.CharField(max_length=30)),
                ("member_name", models.CharField(max_length=20)),
                ("member_gender", models.CharField(max_length=5)),
                ("member_email", models.CharField(max_length=40)),
                ("member_phone", models.CharField(max_length=25)),
                ("member_zipcode", models.CharField(max_length=15)),
                ("member_address1", models.CharField(max_length=100)),
                ("member_address2", models.CharField(default="", max_length=100)),
                ("member_birthday", models.CharField(max_length=15)),
                ("member_point", models.IntegerField(default=1000)),
                ("member_totalPrice", models.IntegerField(default=0)),
                ("reg_date", models.DateField(auto_now_add=True)),
                ("grade_name", models.CharField(default="Bronze", max_length=10)),
            ],
        ),
    ]
