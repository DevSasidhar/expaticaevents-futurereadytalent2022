# Generated by Django 3.2.12 on 2022-04-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_userevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitecodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventid', models.CharField(max_length=20)),
                ('hashcode', models.CharField(max_length=20)),
            ],
        ),
    ]