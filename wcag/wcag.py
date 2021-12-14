from lxml import etree

from wcag.accesskeyvalidator import accesskeyvalidator
from wcag.altvalidator import altvalidator
from wcag.colorvalidator import colorvalidator


class wcag:

    def __init__(self):
        self

    def run_validator(self, html_file):

        htmlparser = etree.HTMLParser()
        tree = etree.parse(html_file, htmlparser)

        validate_alt_wcag = altvalidator()
        validate_alt_wcag.validate_element(tree)

        accesskey_validator = accesskeyvalidator()
        accesskey_validator.validate_element(tree)

        color_validator = colorvalidator()
        color_validator.validate_element(tree)