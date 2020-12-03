def extract(information):
    extracted = information.split(":")
    password = extracted[1]

    policy = extracted[0].split(" ")

    between = policy[0].split("-")
    key = policy[1]

    return (between, key, password.strip())


def valid(information):
    if not information:
        return False
    positions, key, password = extract(information)
    first = int(positions[0]) - 1
    second = int(positions[1]) - 1
    if (password[first] == key) ^ (password[second] == key):
        return True
    return False


if __name__ == "__main__":
    passwords = [
        password
        for password in open("reports.txt", "r").read().split("\n")
        if valid(password)
    ]
    print(passwords)
    print("*" * 10)
    print("Total valid passwords:", len(passwords))
