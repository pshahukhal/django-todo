# Generated by Django 2.2.2 on 2019-06-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todoitems_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='content',
            field=models.TextField(blank=True, default=2),
            preserve_default=False,
        ),
    ]
