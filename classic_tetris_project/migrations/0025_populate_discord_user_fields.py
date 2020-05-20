# Generated by Django 2.2.10 on 2020-05-20 05:21

from django.db import migrations

from classic_tetris_project import discord

def populate_discord_users(apps, schema_editor):
    DiscordUser = apps.get_model('classic_tetris_project', 'DiscordUser')

    for discord_user in DiscordUser.objects.all():
        user_obj = discord.API.user_from_id(discord_user.discord_id)
        discord_user.username = user_obj.name
        discord_user.discriminator = user_obj.discriminator
        discord_user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0024_auto_20200520_0517'),
    ]

    operations = [
        migrations.RunPython(populate_discord_users),
    ]
