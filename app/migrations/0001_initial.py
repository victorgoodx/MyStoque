# Generated by Django 4.1.1 on 2022-10-03 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=30)),
                ('quantidade', models.CharField(max_length=30)),
                ('ano_validade', models.IntegerField()),
            ],
        ),
    ]
