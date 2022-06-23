# Generated by Django 4.0.5 on 2022-06-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_rename_courses_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='height',
            field=models.IntegerField(default=300),
        ),
        migrations.AddField(
            model_name='course',
            name='width',
            field=models.IntegerField(default=260),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/placeholder-image.jpg', height_field=models.IntegerField(default=300), upload_to='courses/%Y/%m/%d', width_field=models.IntegerField(default=260)),
        ),
    ]
