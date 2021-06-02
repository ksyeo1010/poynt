from src.modules.services import RoundService


class RoundController:

    @staticmethod
    def place_user_bet(ctx, title, bet_choice, username, amount):
        guild_id = ctx.guild.id
        RoundService.add_bet(guild_id, title, bet_choice, username, amount)

    @staticmethod
    def add_round(ctx, round_title):
        guild_id = ctx.guild.id
        RoundService.add_round(guild_id, round_title)

    @staticmethod
    def add_choice(ctx, round_title, choice):
        guild_id = ctx.guild.id
        RoundService.add_choice(guild_id, round_title, choice)

    @staticmethod
    def print_predictions(choice, counter):
        return f"{counter}: {choice}"

    @staticmethod
    def get_options(ctx, title):
        guild_id = ctx.guild.id
        return RoundService.get_total_bets(guild_id, title)

    @staticmethod
    def get_round_bets(list_of_dict):
        total_bets = 0
        for option in range(len(list_of_dict)):
            option_bet = list_of_dict[option]["total"]
            total_bets += option_bet
        return total_bets

    @staticmethod
    def get_winning_option_total_bets(list_of_dict, winning_option):
        for option in list_of_dict:
            if option["_id"] == winning_option:
                return option

    @staticmethod
    def get_option_multiplier(winning_option_dict, total_bet):
        return round(1 + (winning_option_dict["total"] / total_bet))

    @staticmethod
    def get_winning_option(ctx, round_title, winning_choice):
        guild_id = ctx.guild.id
        dict_of_options = RoundService.get_round_bets(guild_id, round_title)
        for option in dict_of_options:
            if option["option"] == winning_choice:
                return option

    # @staticmethod
    # def user_payout(ctx, winning_option, multiplier):
    #     guild_id = ctx.guild.id
    #     for user in winning_option["bets"]:
    #         username = user["username"]
    #         amount = user["amount"] * multiplier
    #         RoundService.payout(guild_id, username, amount)

    # list of dictionary, that has each dictionary contains username and amount

    @staticmethod
    def multiplier(ctx, round_title):
        return RoundService.get_total_bets(ctx.guild.id, round_title)

    # get mnultiplier
    # get all the bets of chocies
    # calculate the winning number
    # calculate the username and add amount
