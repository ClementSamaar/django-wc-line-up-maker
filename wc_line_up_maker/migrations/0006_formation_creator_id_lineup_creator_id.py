# Generated by Django 4.1.3 on 2022-12-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc_line_up_maker', '0005_formation_additionnal_info_lineup_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='creator_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lineup',
            name='creator_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
