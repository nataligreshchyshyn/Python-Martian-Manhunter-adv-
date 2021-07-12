import re


def reader():
    with open("django_success.log", "r") as log:
        text = log.readlines()
        lines = "".join(text)
    return lines


def hide_admin(string, pattern):
    with open("django_success.log", "w") as log:
        fixed = re.sub(pattern, "/hiden/", string)
        log.write(fixed)


def change_date(string, pattern):
    with open("django_success.log", "w") as log:
        new_date = re.sub(pattern, "[XX/XXX/XXXX XX:XX:XX]", string)
        log.write(new_date)


if __name__ == "__main__":
    pattern_admin = r"\/admin\/"
    pattern_date = r"\[\d{1,2}\/\w{3}\/\d{4}\s(\d{2}:?){3}\]"
    hide_admin(reader(), pattern_admin)
    change_date(reader(), pattern_date)
