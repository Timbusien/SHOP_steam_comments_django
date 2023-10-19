# Generated by Django 4.2.5 on 2023-10-09 17:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0004_alter_productmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='favorite_by',
            field=models.ManyToManyField(blank=True, related_name='favorite_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='img',
            field=models.FileField(upload_to='items'),
        ),
    ]
