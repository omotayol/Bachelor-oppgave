# Generated by Django 5.0.1 on 2024-03-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("digital_medlemsordning", "0023_activity_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="members",
            name="certificate",
            field=models.ImageField(
                default="certificates/placeholder-image.png",
                null=True,
                upload_to="certificates",
            ),
        ),
    ]