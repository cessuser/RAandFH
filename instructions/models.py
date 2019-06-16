from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Danlin Chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.StringField(label='What is the chance that a block will continue after a period?',
                            choices=[('A','1 in 4'), ('B','2 in 4'),('C','3 in 4'), ('D','4 in 4')],
                            widget=widgets.RadioSelect)
    q2 = models.StringField(label='What is the chance that a block will end after a period?',
                            choices=[('A','1 in 4'), ('B','2 in 4'), ('C','3 in 4'), ('D','4 in 4')],
                            widget=widgets.RadioSelect)
    q3 = models.StringField(label='Will you be in the same group of players in all blocks?',
                            choices=[('A','Yes'), ('B','No'), ('C','I am not sure')],
                            widget=widgets.RadioSelect)
    q4 = models.StringField(label='Will you play as the Firm in all blocks?',
                            choices=[('A', 'Yes'), ('B', 'No'), ('C', 'I am not sure')],
                            widget=widgets.RadioSelect)
    q5 = models.StringField(label='If you are in the Firm group, will you meet the same player from the Investor group twice if a block contains 8 periods?',
                            choices=[('A', 'Yes'), ('B', 'No'), ('C', 'I am not sure')],
                            widget=widgets.RadioSelect)
    q6 = models.StringField(label='If you play as the Firm in one period, and the virtual die shows 6, how can you get a GOOD certificate?',
                            choices=[('A','A.By choosing High only'),
                                     ('B','B.By choosing Low only'),
                                     ('C','C.By choosing either High or Low'),
                                     ('D','D.By not choosing anything')],
                            widget=widgets.RadioSelect)
    q7 = models.StringField(label='If you play as the Firm in one period, and the virtual die shows 3, how can you get a GOOD certificate?',
                            choices=[('A', 'A.By choosing High only'),
                                     ('B', 'B.By choosing Low only'),
                                     ('C', 'C.By choosing either High or Low'),
                                     ('D', 'D.By not choosing anything')],
                            widget=widgets.RadioSelect)
    q8 = models.StringField(label='If you play as the Investor in one period, and you are paired with a Firm with BAD certificate, what does that mean?',
                            choices=[('A','A.The Firm violated the rule last period in this block.'),
                                     ('B','B.The Firm violated the rule at most 2 periods ago in this block.'),
                                     ('C','C.The Firm violated the rule at most 3 periods ago in this block.'),
                                     ('D','D.The Firm violated the rule in some previous period in this block.'),
                                     ('E','E.The Firm violated the rule in some previous period in the previous block.')],
                            widget=widgets.RadioSelect)


