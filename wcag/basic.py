import re


class basic:
    languges = [
        {"lang": "ab", "dir": "rtl"},
        {"lang": "aa", "dir": "rtl"},
        {"lang": "af", "dir": "rtl"},
        {"lang": "ak", "dir": "rtl"},
        {"lang": "sq", "dir": "rtl"},
        {"lang": "am", "dir": "rtl"},
        {"lang": "ar", "dir": "rtl"},
        {"lang": "an", "dir": "rtl"},
        {"lang": "hy", "dir": "rtl"},
        {"lang": "as", "dir": "rtl"},
        {"lang": "av", "dir": "rtl"},
        {"lang": "ae", "dir": "rtl"},
        {"lang": "ay", "dir": "rtl"},
        {"lang": "az", "dir": "rtl"},
        {"lang": "bm", "dir": "rtl"},
        {"lang": "ba", "dir": "rtl"},
        {"lang": "eu", "dir": "rtl"},
        {"lang": "be", "dir": "rtl"},
        {"lang": "bn", "dir": "rtl"},
        {"lang": "bh", "dir": "rtl"},
        {"lang": "bi", "dir": "rtl"},
        {"lang": "bs", "dir": "rtl"},
        {"lang": "br", "dir": "rtl"}, {"lang": "bg", "dir": "rtl"},
        {"lang": "my", "dir": "rtl"},
        {"lang": "ca", "dir": "rtl"},
        {"lang": "ch", "dir": "rtl"},
        {"lang": "ce", "dir": "rtl"},
        {"lang": "ny", "dir": "rtl"},
        {"lang": "zh", "dir": "rtl"},
        {"lang": "zh-Hans", "dir": "rtl"},
        {"lang": "zh-Hant", "dir": "rtl"},
        {"lang": "cv", "dir": "rtl"},
        {"lang": "kw", "dir": "rtl"},
        {"lang": "co", "dir": "rtl"},
        {"lang": "cr", "dir": "rtl"},
        {"lang": "hr", "dir": "rtl"},
        {"lang": "cs", "dir": "rtl"},
        {"lang": "da", "dir": "rtl"},
        {"lang": "dv", "dir": "rtl"},
        {"lang": "nl", "dir": "rtl"},
        {"lang": "dz", "dir": "rtl"},
        {"lang": "en", "dir": "rtl"},
        {"lang": "eo", "dir": "rtl"},
        {"lang": "et", "dir": "rtl"},
        {"lang": "ee", "dir": "rtl"}, {"lang": "fo", "dir": "rtl"},
        {"lang": "fj", "dir": "rtl"},{"lang": "fj", "dir": "rtl"},
        {"lang": "fi", "dir": "rtl"},
        {"lang": "fr", "dir": "rtl"},
        {"lang": "ff", "dir": "rtl"},
        {"lang": "gl", "dir": "rtl"},{"lang": "gd", "dir": "rtl"},
        {"lang": "gv", "dir": "rtl"},
        {"lang": "ka", "dir": "rtl"},
        {"lang": "de", "dir": "rtl"},
        {"lang": "el", "dir": "rtl"},{"lang": "kl", "dir": "rtl"},{"lang": "gn", "dir": "rtl"},{"lang": "gu", "dir": "rtl"},
        {"lang": "ht", "dir": "rtl"},{"lang": "ha", "dir": "rtl"},{"lang": "he", "dir": "rtl"},
        {"lang": "hz", "dir": "rtl"},{"lang": "hi", "dir": "rtl"},{"lang": "ho", "dir": "rtl"},
        {"lang": "hu", "dir": "rtl"},{"lang": "is", "dir": "rtl"},{"lang": "io", "dir": "rtl"},
        {"lang": "ig", "dir": "rtl"},{"lang": "id, in", "dir": "rtl"},{"lang": "ia", "dir": "rtl"},
        {"lang": "ie", "dir": "rtl"},{"lang": "iu", "dir": "rtl"},{"lang": "ik", "dir": "rtl"},
        {"lang": "ga", "dir": "rtl"},{"lang": "it", "dir": "rtl"},{"lang": "ja", "dir": "rtl"},
        {"lang": "jv", "dir": "rtl"},{"lang": "kl", "dir": "rtl"},{"lang": "kn", "dir": "rtl"},
        {"lang": "kr", "dir": "rtl"},{"lang": "ks", "dir": "rtl"},{"lang": "kk", "dir": "rtl"},
        {"lang": "km", "dir": "rtl"},{"lang": "ki", "dir": "rtl"},{"lang": "rw", "dir": "rtl"},
        {"lang": "rn", "dir": "rtl"},{"lang": "ky", "dir": "rtl"},{"lang": "kv", "dir": "rtl"},
        {"lang": "kg", "dir": "rtl"},{"lang": "ko", "dir": "rtl"},{"lang": "ku", "dir": "rtl"},
        {"lang": "kj", "dir": "rtl"},{"lang": "lo", "dir": "rtl"},{"lang": "la", "dir": "rtl"},
        {"lang": "lv", "dir": "rtl"}
    ]

    def __init__(self):
        self

    def isValidURL(self, str):
        # Regex to check valid URL
        regex = ("((http|https)://)(www.)?" +
                 "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                 "{2,256}\\.[a-z]" +
                 "{2,6}\\b([-a-zA-Z0-9@:%" +
                 "._\\+~#?&//=]*)")

        # Compile the ReGex
        p = re.compile(regex)

        # If the string is empty
        # return false
        if (str == None):
            return False

        # Return if the string
        # matched the ReGex
        if (re.search(p, str)):
            return True
        else:
            return False

    def validation(self, tree):

        # H37: Using alt attributes on img elements
        # H2: Combining adjacent image and text links for the same resource
        all_body_images = tree.xpath("/html/body//img")
        for img in all_body_images:
            if img.get('alt') is None:
                img_alt = {
                    "tag": tree.getpath(img),
                    "tag-attrib": img.attrib,
                    "error": "no alt found"
                }
                print("H2 fail", tree.getpath(img))
            elif img.get('alt') == "":
                img_alt = {
                    "tag": tree.getpath(img),
                    "tag-attrib": img.attrib,
                    "error": "no alt found"
                }
                print("H2 fail", tree.getpath(img))
        # H4: Creating a logical tab order through links, form controls, and objects
        inputs = tree.xpath('//input')
        for in_put in inputs:
            if 'tabindex' not in in_put.attrib:
                input_tag = {
                    "tag": tree.getpath(in_put),
                    "tag-attrib": in_put.attrib,
                    "error": "no tabindex found"
                }
                print("H4 fail", tree.getpath(in_put))
        a_tags = tree.xpath('//a')
        for a in a_tags:
            if 'tabindex' not in a.attrib:
                input_tag = {
                    "tag": tree.getpath(a),
                    "tag-attrib": a.attrib,
                    "error": "no tabindex found"
                }
                print("H4 fail", tree.getpath(a))

        # H24: Providing text alternatives for the area elements of image maps
        all_body_area = tree.xpath("/html/body//area")
        for area in all_body_area:
            if area.get('alt') is None:
                img_alt = {
                    "tag": tree.getpath(area),
                    "tag-attrib": area.attrib,
                    "error": "no alt found"
                }
                print("H24 fail:", img_alt)
            elif area.get('alt') == "":
                img_alt = {
                    "tag": tree.getpath(area),
                    "tag-attrib": area.attrib,
                    "error": "no alt found"
                }
                print("H24 fail:", img_alt)
        # H28: Providing definitions for abbreviations by using the abbr element
        abbrs = tree.xpath("/html/body//abbr")
        for abbr in abbrs:
            if abbr.get('title') is None or abbr.get('title') == "":
                print("H28 Fail:", tree.getpath(abbr))

        # H25: Providing a title using the title element
        title = tree.xpath("/html/head/title")
        if title is None and len(title[0].text) == 0:
            print("H25 Fail:", tree.getpath(title), " is not valid ", False)

        # H32: Providing submit buttons
        all_form_tag = tree.xpath("/html//body/form")
        for f in all_form_tag:
            form_valid = False
            for ch in f:
                if ch.tag == "input" and ch.attrib["type"] == "submit":
                    form_valid = True
                if ch.tag == "button" and ch.attrib["type"] == "submit":
                    form_valid = True
                if ch.tag == "image" and ch.attrib["type"] == "submit":
                    form_valid = True
            if form_valid:
                print("H32 fail", tree.getpath(f), " is not valid ", form_valid)

        # H33: Supplementing link text with the title attribute
        a_tags = tree.xpath('//a')
        for a in a_tags:
            if a.get('title') is None or a.get('title') == "":
                print("H33 fail", tree.getpath(a))

        # H34: Using a Unicode right-to-left mark (RLM) or left-to-right mark (LRM) to mix text direction inline

        # H35: Providing text alternatives on applet elements
        applets = tree.xpath('//applet')
        for applet in applets:
            if applet.get('alt') is None or applet.get('alt') == "":
                print("H35 fail", tree.getpath(applet))

        # H36: Using alt attributes on images used as submit buttons
        inputs = tree.xpath('//input')
        for in_put in inputs:
            if in_put.get("alt") is None or in_put.get("alt") == "":
                print("H36 fail", tree.getpath(in_put))

        # H37: Using alt attributes on img elements

        # H39: Using caption elements to associate data table captions with data tables
        tables = tree.xpath('//table')
        for table in tables:
            is_caption = True
            for el in table:
                if el.tag == "caption":
                    is_caption = False
                    break
            if is_caption:
                print("H39 fail", tree.getpath(table))

        # H40: Using description lists

        # H44: Using label elements to associate text labels with form controls
        inputs = tree.xpath('//input')
        for input in inputs:
            id = input.get("id")
            if id is not None:
                lable_found = tree.xpath("//lable[@id = '%s']" % id)
                if lable_found is None:
                    print("H44 fail", tree.getpath(input))
            elif id is None:
                print("H44 fail", tree.getpath(input))

        files = tree.xpath('//file')
        for file in files:
            id = file.get("id")
            if id is not None:
                lable_found = tree.xpath("//lable[@id = '%s']" % id)
                if lable_found is None:
                    print("H44 fail", tree.getpath(file))
            elif id is None:
                print("H44 fail", tree.getpath(file))

        passwords = tree.xpath('//password')
        for password in passwords:
            id = password.get("id")
            if id is not None:
                lable_found = tree.xpath("//lable[@id = '%s']" % id)
                if lable_found is None:
                    print("H44 fail", tree.getpath(password))
            elif id is None:
                print("H44 fail", tree.getpath(password))

        textareass = tree.xpath('//textareas')
        for textareas in textareass:
            id = textareas.get("id")
            if id is not None:
                lable_found = tree.xpath("//lable[@id = '%s']" % id)
                if lable_found is None:
                    print("H44 fail", tree.getpath(textareas))
            elif id is None:
                print("H44 fail", tree.getpath(textareas))

        selects = tree.xpath('//select')
        for select in selects:
            id = select.get("id")
            if id is not None:
                lable_found = tree.xpath("//lable[@id = '%s']" % id)
                if lable_found is None:
                    print("H44 fail", tree.getpath(select))
            elif id is None:
                print("H44 fail", tree.getpath(select))

        # H45: Using longdesc
        images = tree.xpath('//img')
        for img in images:
            if img.get("longdesc") is not None and img.get("src") is not None and self.isValidURL(img.get("src")):
                print("H45 fail", tree.getpath(img))

        # H46: Using noembed with embed
        embeds = tree.xpath('//embed')
        for embed in embeds:
            has_child = True
            for noembeds in embed:
                if noembeds.tag == "noembed":
                    has_child = False
                    break
            if has_child:
                print("H46 fail", tree.getpath(embed))

        # H48: Using ol, ul and dl for lists or groups of links

        # H53: Using the body of the object element
        objects = tree.xpath('//object')
        for object in objects:
            pass
