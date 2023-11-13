# Generated by Django 4.2.4 on 2023-11-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_userprofile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="images/profiles/default.png",
                null=True,
                upload_to="profiles/",
            ),
        ),
    ]
