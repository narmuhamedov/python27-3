# Generated by Django 4.2 on 2023-04-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
