# Generated by Django 2.2.5 on 2019-09-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
