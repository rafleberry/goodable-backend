# Generated by Django 4.0 on 2021-12-15 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_original_video_filename_post_original_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='original_url',
            new_name='mp4_url',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='playback_id',
            new_name='mux_playback_id',
        ),
    ]
