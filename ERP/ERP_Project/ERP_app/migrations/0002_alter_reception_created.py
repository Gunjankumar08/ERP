# Generated by Django 3.2 on 2023-02-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
