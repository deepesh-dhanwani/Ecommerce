# Generated by Django 5.0.7 on 2024-11-26 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0004_featureproduct"),
    ]

    operations = [
        migrations.AlterField(
            model_name="featureproduct",
            name="product_image",
            field=models.FileField(
                default=None, max_length=500, upload_to="featureproduct"
            ),
        ),
    ]
