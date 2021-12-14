import webcolors
from decimal import Decimal as D

WCAG_LUMINOCITY_RATIO_THRESHOLD = {
    "AA": {
        'normal': 4.5,
        'large': 3,
    },
    "AAA": {
        'normal': 7,
        'large': 4.5,
    }
}

TECHNIQUE = {
    "AA": {
        'normal': "G18",
        'large': "G145",
    },
    "AAA": {
        'normal': "G17",
        'large': "G18",
    }
}


def normalise_color(color):
    rgba_color = None
    color = color.split("!", 1)[0].strip()  # remove any '!important' declarations
    color = color.strip(";").strip("}")  # Dang minimisers

    if "transparent" in color or "inherit" in color:
        rgba_color = [0, 0, 0, 0.0]
    elif color.startswith('rgb('):
        rgba_color = list(map(int, color.split('(')[1].split(')')[0].split(', ')))
    elif color.startswith('rgba('):
        rgba_color = list(map(float, color.split('(')[1].split(')')[0].split(', ')))
    else:
        funcs = [
            webcolors.hex_to_rgb,
            webcolors.name_to_rgb,
            webcolors.rgb_percent_to_rgb
        ]

        for func in funcs:
            try:
                rgba_color = list(func(color))
                break
            except:
                continue

    if rgba_color is None:
        rgba_color = [0, 0, 0, 1]
    else:
        rgba_color = (list(rgba_color) + [1])[:4]
    return rgba_color


def calculate_luminocity(r=0, g=0, b=0):
    # Calculates luminocity according to
    # https://www.w3.org/TR/WCAG20-TECHS/G17.html#G17-tests

    x = []
    for C in r, g, b:
        c = C / D('255.0')
        if c < D('0.03928'):
            x.append(c / D('12.92'))
        else:
            x.append(((c + D('0.055')) / D('1.055')) ** D('2.4'))

    R, G, B = x

    L = D('0.2126') * R + D('0.7152') * G + D('0.0722') * B
    return L


def generate_opaque_color(color_stack):
    # http://stackoverflow.com/questions/10781953/determine-rgba-colour-received-by-combining-two-colours

    colors = []
    # Take colors back off the stack until we get one with an alpha of 1.0
    for c in color_stack[::-1]:
        if int(c[3]) == 0:
            continue
        colors.append(c)
        if c[3] == 1.0:
            break

    red, green, blue, alpha = colors[0]

    for r, g, b, a in colors[1:]:
        if a == 0:
            # Skip transparent colors
            continue
        da = 1 - a
        alpha = alpha + a * da
        red = (red * D('0.25') + r * a * da) / alpha
        green = (green * D('0.25') + g * a * da) / alpha
        blue = (blue * D('0.25') + b * a * da) / alpha

    return [int(red), int(green), int(blue)]


def calculate_font_size(font_stack):
    """
    From a list of font declarations with absolute and relative fonts, generate an approximate rendered font-size in point (not pixels).
    """
    font_size = 10  # 10 pt *not 10px*!!

    for font_declarations in font_stack:
        if font_declarations.get('font-size', None):
            size = font_declarations.get('font-size')
        elif font_declarations.get('font', None):
            # Font-size should be the first in a declaration, so we can just use it and split down below.
            size = font_declarations.get('font')

        if 'pt' in size:
            font_size = int(size.split('pt')[0])
        elif 'px' in size:
            font_size = int(size.split('px')[0]) * D('0.75')  # WCAG claims about 0.75 pt per px
        elif '%' in size:
            font_size = font_size * D(size.split('%')[0]) / 100
        # TODO: em and en
    return font_size


def is_font_bold(font_stack):
    """
    From a list of font declarations determine the font weight.
    """
    # Note: Bolder isn't relative!!
    is_bold = False

    for font_declarations in font_stack:
        weight = font_declarations.get('font-weight', "")
        if 'bold' in weight or 'bold' in font_declarations.get('font', ""):
            # Its bold! THe rest of the rules don't matter
            return True
        elif '0' in weight:
            # its a number!
            # Return if it is bold. The rest of the rules don't matter
            return int(weight) > 500  # TODO: Whats the threshold for 'bold'??
        # TODO: What if weight is defined in the 'font' rule?

    return is_bold


def calculate_luminocity_ratio(foreground, background):
    L2, L1 = sorted([
        calculate_luminocity(*foreground),
        calculate_luminocity(*background),
    ])

    return (L1 + D('0.05')) / (L2 + D('0.05'))


def get_applicable_styles(node):
    """
        Generates a list of dictionaries that contains all the styles that *could* influence the style of an element.
        This is the collection of all styles from an element and all it parent elements.
        Returns a list, with each list item being a dictionary with keys that correspond to CSS styles
        and the values are the corresponding values for each ancestor element.
        """
    styles = []
    for parent in node.xpath('ancestor-or-self::*[@style]'):
        style = parent.get('style', "")
        style = style.rstrip(";")

        if not style:
            continue

        styles.append(
            dict([
                tuple(
                    s.strip().split(':', 1)
                )
                for s in style.split(';')
            ])
        )
    return styles


class colorvalidator:

    def __init__(self):
        self

    def skip_element(self, node):
        if node.text is None or node.text.strip() == "":
            return True
        if node.tag in ['script', 'style']:
            return True

    def validate_element(self, tree):
        colors = [[1, 2, 3, 1]]  # Black-ish
        backgrounds = [[254, 253, 252, 1]]  # White-ish
        fonts = [{'font-size': '10pt', 'font-weight': 'normal'}]
        body = tree.xpath("/html/body//*")
        for node in body:
            print(node.text)
            for styles in get_applicable_styles(node):
                if "color" in styles.keys():
                    colors.append(normalise_color(styles['color']))
                if "background-color" in styles.keys():
                    backgrounds.append(normalise_color(styles['background-color']))
                font_rules = {}
                for rule in styles.keys():
                    if 'font' in rule:
                        font_rules[rule] = styles[rule]
                fonts.append(font_rules)
            print(colors, backgrounds)
            font_size = calculate_font_size(fonts)
            font_is_bold = is_font_bold(fonts)
            foreground = generate_opaque_color(colors)
            background = generate_opaque_color(backgrounds)
            ratio = calculate_luminocity_ratio(foreground, background)

            print("color ration ", ratio)

            font_size_type = 'normal'
            # error_code = 'molerat-1'
            # technique = "G18"
            if font_size >= 18 or font_size >= 14 and font_is_bold:
                font_size_type = 'large'
                error_code = 'molerat-2'

            ratio_threshold = WCAG_LUMINOCITY_RATIO_THRESHOLD["AA"][font_size_type]
            # technique = TECHNIQUE[self.level][font_size_type]

            if ratio < ratio_threshold:
                color_error = {
                    "node": node.getroottree().getpath(node),
                    "text": node.text,
                    "Colored text was": colorize(
                        node.text,
                        rgb=int('0x%s' % webcolors.rgb_to_hex(foreground)[1:], 16),
                        bg=int('0x%s' % webcolors.rgb_to_hex(background)[1:], 16),
                    ),
                    "Computed font-size was": str(font_size) + " " + str(['normal', 'bold'][font_is_bold]) + " " + str(
                        font_size_type)
                }
                print("color error:", color_error)
                # disp_text = nice_console_text(node.text)
                # message = (
                #         self.error_codes[error_code] +
                #         u"\n    Computed rgb values are == Foreground {fg} / Background {bg}"
                #         u"\n    Text was:         {text}"
                #         u"\n    Colored text was: {color_text}"
                #         u"\n    Computed font-size was: {font_size} {bold} ({font_size_type})"
                # ).format(
                #     xpath=node.getroottree().getpath(node),
                #     text=disp_text,
                #     fg=foreground,
                #     bg=background,
                #     r=ratio,
                #     font_size=font_size,
                #     bold=['normal', 'bold'][font_is_bold],
                #     font_size_type=font_size_type,
                #     color_text=colorize(
                #         disp_text,
                #         rgb=int('0x%s' % webcolors.rgb_to_hex(foreground)[1:], 16),
                #         bg=int('0x%s' % webcolors.rgb_to_hex(background)[1:], 16),
                #     )
                # )
