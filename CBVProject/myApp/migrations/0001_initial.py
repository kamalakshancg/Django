# Generated by Django 2.2 on 2020-12-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Number', models.IntegerField()),
                ('Marks', models.FloatField()),
                ('Address', models.CharField(max_length=30)),
            ],
        ),
    ]
