# Generated by Django 4.1.3 on 2022-12-26 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wc_line_up_maker', '0006_formation_creator_id_lineup_creator_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='creator_id',
        ),
        migrations.DeleteModel(
            name='SquadList',
        ),
    ]