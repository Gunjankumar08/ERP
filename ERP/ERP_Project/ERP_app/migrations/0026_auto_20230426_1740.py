# Generated by Django 3.2 on 2023-04-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0025_admissions_form_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='busfeediscount',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='classfeediscount',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='extrafeediscount',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='extrafeestructure',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='hostelextrafeediscount',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='hostelextrafeestructure',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='hostelfeediscount',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
