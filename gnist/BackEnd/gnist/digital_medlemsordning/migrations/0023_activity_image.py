# Generated by Django 5.0.1 on 2024-03-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "digital_medlemsordning",
            "0022_alter_members_banned_from_alter_members_banned_until",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="activity_pics"),
        ),
    ]