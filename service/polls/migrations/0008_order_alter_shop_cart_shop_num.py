# Generated by Django 4.1.3 on 2022-12-20 10:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_shop_cart_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=32)),
                ('first_add', models.DateTimeField(auto_now_add=True)),
                ('price', models.CharField(max_length=16)),
                ('shop_list', models.CharField(max_length=256)),
                ('order_status', models.IntegerField()),
                ('courier_name', models.CharField(max_length=16)),
                ('courier_phone', models.CharField(max_length=16)),
                ('courier_place', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='shop_cart',
            name='shop_num',
            field=models.IntegerField(),
        ),
    ]