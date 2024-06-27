# Generated by Django 5.0.1 on 2024-02-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("digital_medlemsordning", "0007_alter_members_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="members",
            name="profile_pic",
            field=models.ImageField(
                null=True, upload_to="gnist/digital_medlemsordning_files/profile_pics"
            ),
        ),
    ]
