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
    between, key, password = extract(information)
    count = sum([1 for char in password if char == key])
    return count >= int(between[0]) and count <= int(between[1])


if __name__ == "__main__":
    passwords = [
        password
        for password in open("reports.txt", "r").read().split("\n")
        if valid(password)
    ]
    print(passwords)
    print("*" * 10)
    print("Total valid passwords:", len(passwords))
