# Generated by Django 4.1.3 on 2022-12-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.CharField(max_length=100),
        ),
    ]
