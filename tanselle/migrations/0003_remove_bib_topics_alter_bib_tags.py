# Generated by Django 4.2.3 on 2023-07-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanselle', '0002_remove_bib_city_alter_bib_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bib',
            name='topics',
        ),
        migrations.AlterField(
            model_name='bib',
            name='tags',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]