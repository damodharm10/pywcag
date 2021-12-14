class altvalidator:

    def __init__(self):
        self

    def validate_element(self, tree):
        all_body_images = tree.xpath("/html/body//img")
        for img in all_body_images:
            if img.get('alt') is None:
                img_alt = {
                    "image_path": tree.getpath(img),
                    "attrib": img.attrib
                }
                print("alt not found", img_alt)
            elif img.get('alt') == "":
                img_alt = {
                    "image_path": tree.getpath(img),
                    "attrib": img.attrib
                }
                print("alt not found", img_alt)
            else:
                pass
