# Generated by Django 4.0.4 on 2022-06-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_alter_userbill_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(default='default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='default.jpg', upload_to=''),
        ),
    ]