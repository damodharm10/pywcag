
class accesskeyvalidator:

    def __init__(self):
        self

    def validate_element(self, tree):
        if len(tree.xpath('/html/body//*[@accesskey]')) == 0:
            print("no access key")
        else:
            pass
