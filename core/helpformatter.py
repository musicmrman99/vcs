from argparse import HelpFormatter

# Based on: https://github.com/byexamples/byexample/blob/master/byexample/cmdline.py
# From: https://discuss.python.org/t/advanced-help-for-argparse/20319/8
class MMHelpFormatter(HelpFormatter):
    __extended_enabled = False

    @classmethod
    def hide_extended(cls):
        cls.__extended_enabled = False

    @classmethod
    def show_extended(cls):
        cls.__extended_enabled = True

    def add_text(self, text, *args, **kwargs):
        if MMHelpFormatter.__extended_enabled:
            HelpFormatter.add_text(self, text, *args, **kwargs)
