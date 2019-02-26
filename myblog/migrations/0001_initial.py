# Generated by Django 2.1.7 on 2019-02-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.PositiveIntegerField(blank=True, null=True)),
                ('ename', models.CharField(blank=True, max_length=50, null=True)),
                ('esal', models.FloatField(blank=True, null=True)),
                ('eadd', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]
