# Generated by Django 3.2 on 2023-03-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0013_busfeediscount_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrafeediscount',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
