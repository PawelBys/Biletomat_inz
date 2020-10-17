# Generated by Django 3.1.2 on 2020-10-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_wyjazdu', models.CharField(max_length=30)),
                ('data_powrotu', models.CharField(max_length=30)),
                ('miasto', models.CharField(max_length=30)),
                ('stopien', models.CharField(max_length=30)),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=30)),
                ('adres', models.CharField(max_length=100)),
                ('pododdzial', models.CharField(max_length=20)),
                ('miesiac', models.CharField(max_length=20)),
                ('kwota', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kwota_slownie', models.CharField(max_length=40)),
            ],
        ),
    ]
