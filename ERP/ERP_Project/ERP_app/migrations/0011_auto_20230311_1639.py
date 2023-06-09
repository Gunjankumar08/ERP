# Generated by Django 3.2 on 2023-03-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0010_receipt_for_extrafee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_for_extrafee',
            name='extra_fee',
            field=models.CharField(default=0, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='receipt_for_extrafee',
            name='extra_fee_dues',
            field=models.CharField(default=0, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='receipt_for_extrafee',
            name='paid_extra_fee',
            field=models.CharField(default=0, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='receipt_for_extrafee',
            name='payable_extra_fee',
            field=models.CharField(default=0, max_length=500, null=True),
        ),
    ]
