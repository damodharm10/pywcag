
class altvalidator:

    def __init__(self):
        self

    def validate_element(self, tree) -> dict:
        all_body_images = tree.xpath("/html/body//img")
        all_body_area = tree.xpath("/html/body//area")
        alts_response = []

        for area in all_body_area:
            if area.get('alt') is None:
                img_alt = {
                    "tag": tree.getpath(area),
                    "tag-attrib": area.attrib,
                    "error": "no alt found"
                }
                print("alt not found", img_alt)
            elif area.get('alt') == "":
                img_alt = {
                    "tag": tree.getpath(area),
                    "tag-attrib": area.attrib,
                    "error": "no alt found"
                }
                alts_response.append(img_alt)
        for img in all_body_images:
            if img.get('alt') is None:
                img_alt = {
                    "tag": tree.getpath(img),
                    "tag-attrib": img.attrib,
                    "error": "no alt found"
                }
                alts_response.append(img_alt)
            elif img.get('alt') == "":
                img_alt = {
                    "tag": tree.getpath(img),
                    "tag-attrib": img.attrib,
                    "error": "no alt found"
                }
                alts_response.append(img_alt)
        return alts_response
