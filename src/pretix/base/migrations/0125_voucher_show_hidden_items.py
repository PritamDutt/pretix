# Generated by Django 2.2.1 on 2019-07-07 10:10

from django.db import migrations, models


def set_show_hidden_items(apps, schema_editor):
    Voucher = apps.get_model('pretixbase', 'Voucher')
    Voucher.objects.filter(quota__isnull=False).update(show_hidden_items=False)

class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0124_seat_seat_guid'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='show_hidden_items',
            field=models.BooleanField(default=True),
        ),
        migrations.RunPython(
            set_show_hidden_items,
            migrations.RunPython.noop,
        )
    ]