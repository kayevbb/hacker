# Generated by Django 2.2.8 on 2019-12-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0002_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='pole',
            name='avatar',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
