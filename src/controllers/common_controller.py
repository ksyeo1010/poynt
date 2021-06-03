from src.modules.services import CommonService, CheckinService


class CommonController:

    @staticmethod
    def initiate_guild(ctx):
        guild_id = ctx.owner.guild.id
        CommonService.init_guild(guild_id)

    @staticmethod
    def check_in_user(ctx, username):
        guild_id = ctx.guild.id
        CheckinService.checkin_user(guild_id, username)

    @staticmethod
    def check_in_time(ctx, username):
        guild_id = ctx.guild.id
        seconds_left = CheckinService.check_time(guild_id, username)
        minute, sec = divmod(seconds_left, 60)
        hour, minute = divmod(minute, 60)
        return "%d:%02d:%02d" % (hour, minute, sec)

