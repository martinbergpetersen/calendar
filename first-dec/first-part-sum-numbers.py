new_sum = 2020


def two_sum(numbers):
    if not numbers:
        return []

    seen = set()

    for number in numbers:
        potential = new_sum - number
        if potential not in seen:
            seen.add(number)
        else:
            return [number, potential], number * potential

    return seen


if __name__ == "__main__":
    numbers = [
        int(number) for number in open("reports.txt", "r").read().split("\n") if number
    ]
    result = two_sum(numbers)

    print(result)
