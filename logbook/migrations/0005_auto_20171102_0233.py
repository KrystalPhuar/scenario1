# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 02:33
from __future__ import unicode_literals

from django.db import migrations
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0004_auto_20171102_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='section',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, autocomplete_view=b'log_section_autocomplete', force_lowercase=True, help_text='Enter a comma-separated tag string', initial=b'coding, documentation, team', to='logbook.Section'),
        ),
        migrations.RemoveField(
            model_name='section',
            name='label',
        ),
        migrations.RemoveField(
            model_name='section',
            name='level',
        ),
        migrations.RemoveField(
            model_name='section',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='section',
            name='path',
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set([('slug',)]),
        ),
    ]