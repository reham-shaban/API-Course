# Generated by Django 4.2 on 2023-04-10 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('littleLemonAPI', '0002_category_menuitem_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='littleLemonAPI.category'),
        ),
    ]
