# Generated by Django 4.0.4 on 2022-05-31 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_userbill'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbill',
            name='discounted_amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbill',
            name='discout',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbill',
            name='total_anount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
            preserve_default=False,
        ),
    ]
