class accesskeyvalidator:

    def __init__(self):
        self

    def validate_element(self, tree):
        inputs = tree.xpath('//input')
        input_responses = []
        for in_put in inputs:
            if 'tabindex' not in in_put.attrib:
                input_tag = {
                    "tag": tree.getpath(in_put),
                    "tag-attrib": in_put.attrib,
                    "error": "no tabindex found"
                }
                input_responses.append(input_tag)
        a_tags = tree.xpath('//a')
        for a in a_tags:
            if 'tabindex' not in a.attrib:
                input_tag = {
                    "tag": tree.getpath(a),
                    "tag-attrib": a.attrib,
                    "error": "no tabindex found"
                }
                input_responses.append(input_tag)
        return input_responses
