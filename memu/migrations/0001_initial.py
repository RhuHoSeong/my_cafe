# Generated by Django 4.2.5 on 2023-10-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='memu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('size', models.CharField(choices=[('big', 'big'), ('small', 'small')], default='small', max_length=10)),
                ('price', models.IntegerField(null=True)),
                ('temp', models.CharField(choices=[('hot', 'hot'), ('ice', 'ice')], default='hot', max_length=3)),
            ],
        ),
    ]
