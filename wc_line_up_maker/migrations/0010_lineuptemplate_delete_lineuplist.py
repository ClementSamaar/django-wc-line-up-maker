# Generated by Django 4.1.3 on 2022-12-26 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wc_line_up_maker', '0009_remove_lineuplist_player_remove_lineuplist_position_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineUpTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_up', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='line_up_template', to='wc_line_up_maker.lineup')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='line_up_template', to='wc_line_up_maker.player')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='line_up_template', to='wc_line_up_maker.position')),
            ],
        ),
        migrations.DeleteModel(
            name='LineUpList',
        ),
    ]
