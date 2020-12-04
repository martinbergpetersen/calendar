import re


def rules(items):
    byr = items["byr"]
    if int(byr) >= 1920 and int(byr) <= 2002:
        pass
    else:
        return False

    iyr = items["iyr"]
    if int(iyr) >= 2010 and int(iyr) <= 2020:
        pass
    else:
        return False

    eyr = items["eyr"]
    if len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030:
        pass
    else:
        return False

    hgt = items["hgt"]
    if "cm" in hgt:
        height = hgt[:3]
        if height.isdigit():
            if int(height) >= 150 and int(height) <= 193:
                pass
            else:
                return False
        else:
            return False
    else:
        height = hgt[:2]
        if int(height) >= 59 and int(height) <= 76:
            pass
        else:
            return False

    pattern = re.compile("^#[a-z0-9]{6}$")
    hcl = items["hcl"]
    if pattern.match(hcl):
        pass
    else:
        return False
    ecl = items["ecl"]
    if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        pass
    else:
        return False
    pid = items["pid"]
    pattern = re.compile(r"^\d{9}$")
    if pattern.match(pid):
        pass
    else:
        return False
    return True


def scan(passport):
    optional = "cid"

    fields = passport.strip().replace("\n", " ").split(" ")
    values = {}
    for field in fields:
        key, value = field.split(":")
        values[key] = value
    if len(fields) == 8:
        if rules(values):
            return True
    elif len(fields) == 7 and optional not in values:
        if rules(values):
            return True
    return False


if __name__ == "__main__":
    with open("reports.txt") as f:
        passports = f.read().split("\n\n")
    result = [passport.replace("\n", " ") for passport in passports if scan(passport)]

    print(result)
    print("*" * 20)
    print(len(result))
