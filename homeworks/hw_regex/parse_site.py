import json
import re
import requests


def get_departments_info(section_pattern, contacts_pattern, text, result=None):
    if not result:
        result = {}
    is_section = []
    for line in text.split("\n"):
        match_section = re.search(section_pattern, line)
        match_contacts = re.search(contacts_pattern, line)

        if match_section:
            section = match_section.group("section")
            result[section] = []
            is_section.append(section)
        elif match_contacts:
            department = match_contacts.group("department")
            email = match_contacts.group("email")
            target_section = is_section[-1]
            result[target_section].append((department, email))
    return result


if __name__ == "__main__":
    data = requests.get(
        "http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80"
        "%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1"
        "%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83"
        "%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0"
        "%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83")
    html = data.content.decode("utf-8", "strict")
    replacements = [(r"\s{2,}", " "), (r"\n<b>", " <b>")]
    for pat, repl in replacements:
        fixed_html = re.sub(pat, repl, html)
    section_pattern = r"\d{1,2}\.\s(?P<section>\w[\w\s\,\-]+[\w\.])"
    contacts_pattern = r"(?P<department>\w[\w\-\,\.\s\"]+[\w\"\.])[\s<b>]+(?P<email>[\w_]+@vsau\.vin\.ua)"
    structure = get_departments_info(section_pattern, contacts_pattern, fixed_html)
    with open("result.json", "w") as f:
        json.dump(structure, f, ensure_ascii=False, indent=4, sort_keys=True)
