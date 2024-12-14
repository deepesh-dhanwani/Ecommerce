# Generated by Django 5.0.7 on 2024-11-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="homepageright",
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
                ("homepageright_text", models.TextField()),
                (
                    "homepageright_img",
                    models.FileField(
                        default=None,
                        max_length=500,
                        null=True,
                        upload_to="homepageright",
                    ),
                ),
            ],
        ),
    ]
