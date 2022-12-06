# Generated by Django 4.1.3 on 2022-11-10 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('goal', models.CharField(max_length=100)),
                ('activity_level', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('location', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('weekly_goal', models.DecimalField(
                    decimal_places=2, max_digits=4)),
            ],
        ),
    ]