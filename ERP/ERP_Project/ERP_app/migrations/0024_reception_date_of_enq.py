# Generated by Django 3.2 on 2023-03-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0023_alter_hostel_receipt_hostel_fee_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='date_of_enq',
            field=models.DateField(null=True),
        ),
    ]
