# Generated by Django 4.2 on 2023-04-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cep', models.IntegerField(max_length=100)),
                ('senha', models.IntegerField(max_length=100)),
            ],
        ),
    ]
