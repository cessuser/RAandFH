from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class GeneralInfo(Page):
    pass


class Blocks(Page):
    pass


class Periods(Page):
    pass


class Matching(Page):
    pass


class Game(Page):
    def vars_for_template(self):
        high_in = '2, 2'
        high_not = '0, 1'
        low_in = '4, 0'
        low_not = '1, 1'
        if self.session.vars['RA']:
            high_in = '1, 1'
            high_not = '-1, 0'
            low_in = '3, -1'
            low_not = '0, 0'

        return{
            'high_inv': high_in,
            'high_not': high_not,
            'low_in': low_in,
            'low_not': low_not
        }


class Certificates(Page):
    def is_displayed(self):
        return self.session.config['trt'] == 'RA'


class BeforeGame(Page):
    def is_displayed(self):
        return self.session.config['trt'] == 'RA'

class BeforeGame_FH(Page):
    def is_displayed(self):
        return self.session.config['trt'] == 'FH'


class AfterGame(Page):
    pass


class Comprehension(Page):
    pass

page_sequence = [
    GeneralInfo,
    Blocks,
    Periods,
    Matching,
    Game,
    Certificates,
    BeforeGame,
    BeforeGame_FH,
    AfterGame,
    Comprehension
]
