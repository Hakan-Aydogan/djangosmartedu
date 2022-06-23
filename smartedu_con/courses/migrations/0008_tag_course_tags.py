# Generated by Django 4.0.5 on 2022-06-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_category_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]
