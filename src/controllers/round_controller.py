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
    def is_prediction_running(ctx, round_title):
        guild_id = ctx.guild.id
        return RoundService.check_round(guild_id, round_title)

    @staticmethod
    def change_prediction_status(ctx, round_title, is_voting_on):
        guild_id = ctx.guild.id
        RoundService.set_round_state(guild_id, round_title, is_voting_on)

    @staticmethod
    def post_predictions(ctx, round_title):
        guild_id = ctx.guild.id
        result = RoundService.get_total_bets(guild_id, round_title)
        pair_list = []
        for option in result:
            pair = f"'{option.option}' currently has {option.total} points in the pool!"
            pair_list.append(pair)
        options_string = '\n'.join(pair_list)
        return options_string

    # @staticmethod
    # def get_options(ctx, title):
    #     guild_id = ctx.guild.id
    #     return RoundService.get_total_bets(guild_id, title)

    # @staticmethod
    # def get_total_round_bets(list_of_dict):
    #     total_bets = 0
    #     for option in range(len(list_of_dict)):
    #         option_bet = list_of_dict[option]["total"]
    #         total_bets += option_bet
    #     return total_bets

    @staticmethod
    def multiplier_total_pool(ctx, title, money):
        guild_id = ctx.guild.id
        list_of_options = RoundService.get_total_bets(guild_id, title)
        list_strings = []
        total_bets = 0
        for option in list_of_options:
            option_bet = option.total
            total_bets += option_bet
        for option in list_of_options:
            check_multiplier_option = option.username
            option_multiplier = round(1 + (((total_bets + money) - (option.total + money)) / (total_bets + money)))
            apply_multiplier = option_multiplier * money
            list_strings.append(f"If you bet {money} points on '{check_multiplier_option}' right now, you can get "
                                f"{apply_multiplier} points if you win!")
        return list_strings

    # @staticmethod
    # def get_winning_option_total_bets(list_of_dict, winning_option):
    #     for option in list_of_dict:
    #         if option["_id"] == winning_option:
    #             return option

    @staticmethod
    def get_option_multiplier(ctx, round_title, winning_choice):
        guild_id = ctx.guild.id
        list_of_options = RoundService.get_total_bets(guild_id, round_title)
        total_bets = 0
        for option in list_of_options:
            option_bet = option.total
            total_bets += option_bet
        win_option = RoundService.get_round_bets(guild_id, round_title, winning_choice)
        return round(1 + ((total_bets - win_option[0].amount) / total_bets))

    @staticmethod
    def get_winning_option(ctx, round_title, winning_choice):
        guild_id = ctx.guild.id
        dict_of_options = RoundService.get_round_bets(guild_id, round_title, winning_choice)
        return dict_of_options

    @staticmethod
    def apply_multiplier(winner, multiplier):
        winner.amount *= multiplier
        return winner
