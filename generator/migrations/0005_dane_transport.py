# Generated by Django 3.1.2 on 2020-10-27 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_dane_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='dane',
            name='transport',
            field=models.CharField(default='pociag', max_length=30),
            preserve_default=False,
        ),
    ]