# Generated by Django 2.1.4 on 2018-12-05 01:08

from django.db import migrations


def create_data(apps, schema_editor):
    customer = apps.get_model('customers', 'Customer')
    customer(first_name="Customer 001", last_name="Customer 001", email="customer001@email.com", phone="00000000",
             address="Customer 000 Address", description="Customer 001 description").save()


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
