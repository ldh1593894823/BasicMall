# Generated by Django 4.1.3 on 2023-02-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_order_evaluation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_number',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='delivery_address',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_gender',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]