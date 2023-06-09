# Generated by Django 3.2 on 2023-02-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0008_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='bus_dues',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='bus_fee',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='bus_paid_fee',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='bus_payable_fee',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='discounted_bus_fee',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
