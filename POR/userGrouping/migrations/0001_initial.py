# Generated by Django 3.2.7 on 2021-09-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_gpu', models.CharField(max_length=100)),
                ('memory_type', models.CharField(max_length=100)),
                ('board_name', models.CharField(max_length=100)),
                ('ROM_name', models.CharField(max_length=100)),
            ],
        ),
    ]
