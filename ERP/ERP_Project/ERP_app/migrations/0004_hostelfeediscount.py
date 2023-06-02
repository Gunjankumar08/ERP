# Generated by Django 3.2 on 2023-02-26 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_app', '0003_classfeediscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelFeeDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_name', models.CharField(max_length=50, null=True)),
                ('month', models.CharField(max_length=50, null=True)),
                ('main_amount', models.CharField(max_length=500, null=True)),
                ('discounted_amount', models.CharField(max_length=500, null=True)),
                ('final_amount', models.CharField(max_length=50, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('admission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hostelFeeDiscount', to='ERP_app.admissions_form')),
            ],
        ),
    ]
