# Generated by Django 4.0.4 on 2022-05-31 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=1000)),
                ('products', models.CharField(max_length=10000)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
