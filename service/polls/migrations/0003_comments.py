# Generated by Django 4.1.3 on 2022-12-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_shop_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=64)),
            ],
        ),
    ]