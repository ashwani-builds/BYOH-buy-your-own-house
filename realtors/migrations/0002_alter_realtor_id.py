# Generated by Django 3.2.6 on 2021-08-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("realtors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="realtor",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
