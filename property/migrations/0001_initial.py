# Generated by Django 5.0 on 2023-12-25 10:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Specify the name of the category.', max_length=255, verbose_name='Name of property')),
                ('features', models.TextField(blank=True, default='', help_text='Specify features or amenities of property.', verbose_name='Features of Property')),
                ('address', models.TextField(help_text='Specify the address of the property.', verbose_name='Address of property')),
                ('location', models.URLField(blank=True, default='', help_text='Google Maps Link (Optional).', verbose_name='Google map of property')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
                'ordering': ['-created_at'],
            },
        ),
    ]