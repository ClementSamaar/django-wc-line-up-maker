# Generated by Django 4.1.3 on 2022-12-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc_line_up_maker', '0004_remove_lineup_formation_remove_lineup_squad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='additionnal_info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lineup',
            name='name',
            field=models.CharField(default='LineUp', max_length=200),
            preserve_default=False,
        ),
    ]
