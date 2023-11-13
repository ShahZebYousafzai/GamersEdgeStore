# Generated by Django 4.2.4 on 2023-11-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_profile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="profiles/default.png",
                null=True,
                upload_to="profiles/",
            ),
        ),
    ]