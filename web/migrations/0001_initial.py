# Generated by Django 4.0.2 on 2022-12-31 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('lat', models.CharField(max_length=200)),
                ('lng', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]