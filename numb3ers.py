import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    Explain of the Regular Expression:
    1. 25[0-5] to check the pattern 25x
    2. 2[0-4][0-9] to check the pattern 200 - 249
    3. [01]?[0-9][0-9]? to check the pattern 0 - 199
    4. (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.) make group of the above patterns
    5. ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3} repeat 3 times of the group
    6. ^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
        After 3 times of the repetion (xxx.xxx.xxx.) follow by (xxx)
    """
    if re.search(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        return True
    return False


if __name__ == "__main__":
    main()
