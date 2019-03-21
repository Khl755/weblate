# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 08:22
from __future__ import unicode_literals

from django.db import migrations


def fix_repo_scope(apps, schema_editor):
    Addon = apps.get_model('addons', 'Addon')
    Addon.objects.filter(name='weblate.git.squash').update(repo_scope=True)


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0012_addon_repo_scope'),
    ]

    operations = [
        migrations.RunPython(fix_repo_scope),
    ]
