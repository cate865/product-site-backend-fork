# Generated by Django 4.0.6 on 2022-07-13 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listed_properties', '0002_remove_propertyimages_image_url_propertyimages_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listedproperties',
            old_name='property_type_id',
            new_name='propertytypeid',
        ),
        migrations.RenameField(
            model_name='listedproperties',
            old_name='user_id',
            new_name='userid',
        ),
    ]
