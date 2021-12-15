from wcag.wcag import wcag


def main():
    wcag_obj = wcag()
    response = wcag_obj.run_validator(html_file="test-data/test1.html")
    print(response)


if __name__ == "__main__":
    main()
