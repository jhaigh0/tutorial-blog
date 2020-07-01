# Generated by Django 2.2.13 on 2020-06-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_cv_element_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dated_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ended', models.BooleanField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Text_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Titled_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('text', models.TextField()),
            ],
        ),
    ]