from lxml import etree

from wcag.accesskeyvalidator import accesskeyvalidator
from wcag.altvalidator import altvalidator
from wcag.basic import basic
from wcag.colorvalidator import colorvalidator


class wcag:

    def __init__(self):
        self

    def run_validator(self, html_file) -> dict:
        htmlparser = etree.HTMLParser()
        tree = etree.parse(html_file, htmlparser)

        basic_obj = basic()
        response_basic = basic_obj.validation(tree)

        # validate_alt_wcag = altvalidator()
        # response = validate_alt_wcag.validate_element(tree)
        #
        # accesskey_validator = accesskeyvalidator()
        # access_keys_response = accesskey_validator.validate_element(tree)
        #
        # color_validator = colorvalidator()
        # color_validator.validate_element(tree)

        print(response_basic)

        #return {"alts": response, "access_keys": access_keys_response}
