from wcag.wcag import wcag


def main():
    wcag_obj = wcag()
    wcag_obj.run_validator(html_file="test-data/test1.html")


if __name__ == "__main__":
    main()
