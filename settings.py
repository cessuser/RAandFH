from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 4.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'RA',
        'display_name': "RA",
        'num_demo_participants': 16,
        'trt': 'RA',
       'app_sequence': ['Game'],
    },
    {
        'name': 'FH',
        'display_name': "FH",
        'num_demo_participants': 4,
        'trt': 'FH',
       'app_sequence': ['Game'],
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'ECUs'

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '0t42-*oq8)7e2s+zhujzrin7(=raz^!!5c7+&6^!h4-7bqixa#'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
