# Generated by Django 3.2 on 2023-03-15 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0016_alter_receipt_previous_paid_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='previous_paid_amount',
            new_name='previous_bill_paid_amount',
        ),
    ]
