# Generated by Django 4.2.6 on 2023-11-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_payment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
