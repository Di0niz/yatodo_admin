# Generated by Django 4.2.16 on 2024-12-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={
                "ordering": ["date"],
                "verbose_name": "Event",
                "verbose_name_plural": "Events",
            },
        ),
        migrations.AddField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[("webinar", "Webinar"), ("mentor_session", "Mentor Session")],
                default="webinar",
                max_length=20,
                verbose_name="Event Type",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="date",
            field=models.DateTimeField(verbose_name="Date"),
        ),
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Name"),
        ),
    ]