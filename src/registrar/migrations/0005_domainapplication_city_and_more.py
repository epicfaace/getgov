# Generated by Django 4.1.3 on 2022-12-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrar", "0004_domainapplication_federal_agency"),
    ]

    operations = [
        migrations.AddField(
            model_name="domainapplication",
            name="city",
            field=models.TextField(blank=True, help_text="City", null=True),
        ),
        migrations.AddField(
            model_name="domainapplication",
            name="urbanization",
            field=models.TextField(blank=True, help_text="Urbanization", null=True),
        ),
    ]
