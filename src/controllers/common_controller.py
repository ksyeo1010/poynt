from src.modules.services import CommonService


class CommonController:

    @staticmethod
    def initiate_guild(ctx):
        guild_id = ctx.owner.guild.id
        CommonService.init_guild(guild_id)
