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
    pass


class Certificates(Page):
    pass


class BeforeGame(Page):
    pass


class AfterGame(Page):
    pass


class Comprehension(Page):
    # form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8']
    # form_fields = ['q1']
    form_model = models.Player

    def q1_error_message(self, value):
        if value != 'C':
            return 'Try again.'

    # def q2_error_message(self, value):
    #     if value != 'A':
    #         return 'Try again.'
    #
    # def q3_error_message(self, value):
    #     if value != 'B':
    #         return 'Try again.'
    #
    # def q4_error_message(self, value):
    #     if value != 'B':
    #         return 'Try again.'
    #
    # def q5_error_message(self, value):
    #     if value != 'B':
    #         return 'Try again.'
    #
    # def q6_error_message(self, value):
    #     if value != 'A':
    #         return 'Try again.'
    #
    # def q7_error_message(self, value):
    #     if value != 'C':
    #         return 'Try again.'
    #
    # def q8_error_message(self, value):
    #     if value != 'D':
    #         return 'Try again.'

    def vars_for_template(self):
        pass

page_sequence = [
    # GeneralInfo,
    # Blocks,
    # Periods,
    # Matching,
    # Game,
    # Certificates,
    # BeforeGame,
    # AfterGame,
    Comprehension
]
