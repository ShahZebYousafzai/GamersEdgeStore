# Generated by Django 4.2.6 on 2024-01-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_gameorder_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='downloads',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]