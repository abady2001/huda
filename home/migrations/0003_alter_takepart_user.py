# Generated by Django 4.1 on 2022-09-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_takepart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takepart',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
