# Generated by Django 4.2 on 2023-04-10 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littleLemonAPI', '0003_alter_menuitem_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category_id',
        ),
    ]
