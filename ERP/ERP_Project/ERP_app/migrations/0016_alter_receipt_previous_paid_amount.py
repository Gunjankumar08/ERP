# Generated by Django 3.2 on 2023-03-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0015_receipt_previous_paid_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='previous_paid_amount',
            field=models.CharField(default=0, max_length=500, null=True),
        ),
    ]
