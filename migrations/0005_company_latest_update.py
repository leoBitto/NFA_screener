# Generated by Django 4.1.7 on 2023-03-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screener', '0004_company_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='latest_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]