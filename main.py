from config import DiscordConfig, SupabaseConfig, GSheetConfig
from connections import GSheetInstance, SupabaseInstance
from config import GSheetConfig, SupabaseConfig
from bot_functionality import *
from sync_commands import sync_commands


def main():
    gsheet_config = GSheetConfig()
    supabase_config = SupabaseConfig()
    discord_config = DiscordConfig()

    supabase_instance = SupabaseInstance(
        api_url=supabase_config.get_api_url(), supabase_key=supabase_config.get_key())

    gsheet_client = GSheetInstance(
        credentials_filename=gsheet_config.get_credentials_filename(), spreadsheet_key=gsheet_config.get_spreadsheet_key())
    supabase_client = supabase_instance.get_instance()

    discord_client = DiscordClient(guild_id=discord_config.get_guild_id())
    embed_factory = Embeds()
    discord_client = sync_commands(discord_client=discord_client, gsheet_client=gsheet_client, supabase_client=supabase_client,
                                   embed_factory=embed_factory)

    discord_client.run(discord_config.get_token())


if __name__ == "__main__":
    main()
