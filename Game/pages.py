from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import math


class BlockBegin(Page):
    def is_displayed(self):
        return self.round_number % Constants.one_blk_len == 1 and self.subsession.if_continue

    def vars_for_template(self):
        return {
            'half_subjects': int(len(self.session.get_participants())/2),
            'role': self.player.role()
        }


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.if_continue

    def vars_for_template(self):
        match_role = "Firm"
        if self.player.role() == 'Firm':
            match_role = 'Investor'
        period = self.round_number
        if period % Constants.one_blk_len != 0:
            period = period % Constants.one_blk_len
        else:
            period = Constants.one_blk_len
        return{
            'match_role': match_role,
            'period': period
        }


class DiceRolling(Page):
    form_fields = ['virtual_dice']
    form_model = models.Player

    def is_displayed(self):
        return self.player.role() == 'Firm' and self.subsession.if_continue


class DiceResult(Page):
    def is_displayed(self):
        return self.player.role() == 'Firm' and self.subsession.if_continue

    def vars_for_template(self):
        msg = 'Therefore, you will only receive a GOOD certificate if you choose High in this period.'
        if self.session.config['trt'] == 'RA':
            if self.player.virtual_dice < 5:
                msg = 'Therefore, you will receive a GOOD certificate regardless of what you choose in this period.'
        else:
            msg = ''
        return {
            'dice_value': self.player.virtual_dice,
            'msg': msg
        }


class HighorLow(Page):
    form_model = models.Player

    def is_displayed(self):
        return self.subsession.if_continue

    def get_form_fields(self):
        if self.player.role() == 'Firm':
            return ['High_Low']
        else:
            return ['If_Invest']

    def vars_for_template(self):
        msg = ''
        if self.session.config['trt'] == 'RA':
            if self.player.role() == 'Firm':
                msg = 'Therefore, you will only receive a GOOD certificate if you choose High in this period.'
                if self.player.virtual_dice < 5:
                    msg = 'Therefore, you will receive a GOOD certificate regardless of what you choose in this period.'

        return {
            'dice_value': self.player.virtual_dice,
            'msg': msg
        }


class WaitForFirm(WaitPage):
    body_text = "Please wait for the Firm to roll the die."

    def is_displayed(self):
        return self.subsession.if_continue


class WaitForInvestor(WaitPage):
    def is_displayed(self):
        return self.subsession.if_continue


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.subsession.if_continue

    def after_all_players_arrive(self):
        if self.session.config['trt'] == 'RA':
            self.group.set_certificate()
        self.group.set_payoff()


class PeriodEnd(Page):
    def is_displayed(self):
        return self.subsession.if_continue

    def vars_for_template(self):
        period = self.round_number
        if period % Constants.one_blk_len != 0:
            period = period % Constants.one_blk_len
        else:
            period = Constants.one_blk_len
        return {
            'period': period
        }


class FirmCertificate(Page):
    def is_displayed(self):
        return self.player.role() == 'Investor' and self.round_number > 1 and self.session.config['trt'] == 'RA' and self.subsession.if_continue

    def vars_for_template(self):
        other_player = self.group.get_player_by_role('Firm')

        return{
            'last_certificate': other_player.in_round(self.round_number-1).certificate
        }


class FirmHighLownum(Page):
    def is_displayed(self):
        return self.session.config['trt'] == 'FH' and self.round_number % Constants.one_blk_len != 1 and self.player.role() == 'Investor' and self.subsession.if_continue

    def vars_for_template(self):
        firm = self.group.get_player_by_role('Firm')
        blk_begin = math.floor((self.round_number - 1) / Constants.one_blk_len)* Constants.one_blk_len
        history = [f.High_Low for f in firm.in_previous_rounds()][blk_begin:]

        print('blk begin: ', blk_begin)
        high = history.count('High')
        low = history.count('Low')

        firm.High_num = high
        firm.Low_num = low

        return {
            'high': high,
            'low': low
        }


class WaitForAll(WaitPage):
    wait_for_all_groups = True

    def vars_for_template(self):
        if self.round_number == 1:
            body_text = "Please wait for other players to enter current block."
        elif self.round_number % Constants.one_blk_len == 1:
            body_text = "Please wait for other players to finish their current block."
        else:
            body_text = "Please wait for other players to finish their current period."

        self.subsession.set_if_continue()
        return {'body_text': body_text}


class ExperimentEnd(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.set_chosen_blk()
        self.player.set_total_payoff()
        return {
            'chosen_blk': self.player.chosen_blk,
            'blk_real_pay': self.player.blk_total_payoff.to_real_world_currency(self.session),
            'total_real_pay': self.player.total_payoff
        }
page_sequence = [
    WaitForAll,
    BlockBegin,
    Introduction,
    FirmCertificate,
    FirmHighLownum,
    WaitForInvestor,
    DiceRolling,
    DiceResult,
    WaitForFirm,
    HighorLow,
    ResultsWaitPage,
    PeriodEnd,
    ExperimentEnd
]
