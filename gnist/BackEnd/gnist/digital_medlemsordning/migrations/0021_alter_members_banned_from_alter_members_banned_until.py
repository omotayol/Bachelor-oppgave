# Generated by Django 5.0.1 on 2024-03-10 20:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "digital_medlemsordning",
            "0020_suggestionbox_description_suggestionbox_title",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="members",
            name="banned_from",
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name="members",
            name="banned_until",
            field=models.DateField(blank=True, default=None),
        ),
    ]
