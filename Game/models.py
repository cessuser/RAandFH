from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import math
author = 'Danlin Chen'

doc = """
Review Aggregator or Full History
"""


class Constants(BaseConstants):
    name_in_url = 'Game'
    players_per_group = 2
    num_blk = 30
    one_blk_len = 8
    num_rounds = one_blk_len * num_blk


class Subsession(BaseSubsession):
    if_continue = models.BooleanField()

    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['history_firms'] = [0 for i in range(0, Constants.num_blk)]
        if self.round_number % Constants.one_blk_len == 1:
            player_lst = [i for i in range(1,int(len(self.get_players()))+1)]
            random.shuffle(player_lst)
            self.session.vars['firms'] = player_lst[0:int(len(player_lst)/2)]
            self.session.vars['investors'] = player_lst[int(len(player_lst)/2):]
            cur_blk = math.floor((self.round_number - 1)/Constants.one_blk_len)
            self.session.vars['history_firms'][cur_blk] = self.session.vars['firms']
            print('firms ', self.session.vars['firms'])
            print('investors ', self.session.vars['investors'])


        mtx = []
        assert(len(self.session.vars['firms']) == len(self.session.vars['investors']))
        for i in range(0, int(len(self.session.vars['firms']))):
            mtx.append([self.session.vars['firms'][i], self.session.vars['investors'][i]])
        self.set_group_matrix(mtx)
        self.session.vars['investors'] = self.session.vars['investors'][1:] + self.session.vars['investors'][0:1]
        print('round number: ', self.round_number, ' groups: ', self.get_group_matrix())

    def set_if_continue(self):
        if self.round_number % Constants.one_blk_len == 1:
            self.if_continue = True
        else:
            random_num = [1,2,3,4]
            random.shuffle(random_num)
            if self.round_number % Constants.one_blk_len == 0:
                self.if_continue = False
            else:
                if random_num[0] == 4:
                    self.if_continue = False
                else:
                    self.if_continue = True


class Group(BaseGroup):
    def set_certificate(self):
        Firm = self.get_player_by_role('Firm')
        if Firm.virtual_dice < 5:
            Firm.certificate = 'GOOD'
        else:
            if Firm.High_Low == 'High':
                Firm.certificate = 'GOOD'
            else:
                Firm.certificate = 'BAD'

    def set_payoff(self):
        Firm = self.get_player_by_role('Firm')
        Investor = self.get_player_by_role('Investor')

        if Firm.High_Low == 'High':
            if Investor.If_Invest == 'Invest':
                Firm.payoff = c(2)
                Investor.payoff = c(2)
                if self.session.config['trt'] == 'RA':
                    Firm.payoff = c(1)
                    Investor.payoff = c(1)
            else:
                Firm.payoff = c(0)
                Investor.payoff = c(1)
                if self.session.config['trt'] == 'RA':
                    Firm.payoff = c(-1)
                    Investor.payoff = c(0)
        else:
            if Investor.If_Invest == 'Invest':
                Firm.payoff = c(4)
                Investor.payoff = c(0)
                if self.session.config['trt'] == 'RA':
                    Firm.payoff = c(3)
                    Investor.payoff = c(-1)
            else:
                Firm.payoff = c(1)
                Investor.payoff = c(1)
                if self.session.config['trt'] == 'RA':
                    Firm.payoff = c(0)
                    Investor.payoff = c(0)



class Player(BasePlayer):
    virtual_dice = models.IntegerField(min=1, max=6)
    High_Low = models.StringField(choices=['High', 'Low'], widget=widgets.RadioSelect,
                                  label='Please choose between the following two options.')
    If_Invest = models.StringField(choices=['Invest', 'Not Invest'], widget=widgets.RadioSelect,
                                   label='Please choose between the following two options.')
    certificate = models.StringField()
    chosen_blk = models.IntegerField(min=1, max=Constants.num_blk)
    blk_total_payoff = models.CurrencyField()
    total_payoff = models.IntegerField()

    High_num = models.IntegerField()
    Low_num = models.IntegerField()

    def role(self):
        cur_firms = self.session.vars['history_firms'][math.floor((self.round_number-1)/Constants.one_blk_len)]
        if self.id_in_subsession in cur_firms:
            return 'Firm'
        else:
            return 'Investor'

    def set_chosen_blk(self):
        self.chosen_blk = random.randint(1, Constants.num_blk)

    def set_total_payoff(self):
        begin_round = int((self.chosen_blk-1)*Constants.one_blk_len+1)
        end_round = int(self.chosen_blk * Constants.one_blk_len)
        blk_old_player = self.in_rounds(begin_round, end_round)
        self.blk_total_payoff = sum([p.payoff for p in blk_old_player])
        self.total_payoff = int(self.blk_total_payoff.to_real_world_currency(self.session) \
                            + self.session.config['participation_fee'])


