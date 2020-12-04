def scan(passport):
    optional = "cid"

    fields = passport.strip().replace("\n", " ").split(" ")
    values = {}
    for field in fields:
        key, value = field.split(":")
        values[key] = value
    if len(fields) == 8:
        return True
    elif len(fields) == 7 and optional not in values:
        return True
    return False


if __name__ == "__main__":
    with open("reports.txt") as f:
        passports = f.read().split("\n\n")
    result = [passport.replace("\n", " ") for passport in passports if scan(passport)]

    print(result)
    print("*" * 20)
    print(len(result))
