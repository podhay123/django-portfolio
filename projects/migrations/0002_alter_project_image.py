# Generated by Django 4.1.3 on 2022-11-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FilePathField(path="/projects/img"),
        ),
    ]
