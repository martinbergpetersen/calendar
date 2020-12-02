new_sum = 2020


def three_sum(numbers):
    numbers.sort()

    for i in range(len(numbers) - 2):
        left = i + 1
        right = len(numbers) - 1
        while left < right:
            current = numbers[i] + numbers[left] + numbers[right]
            if current == new_sum:
                result = [numbers[i], numbers[left], numbers[right]]
                return (result, result[0] * result[1] * result[2])
            elif current < new_sum:
                left += 1
            elif current > new_sum:
                right -= 1

    return []


if __name__ == "__main__":
    numbers = [
        int(number) for number in open("reports.txt", "r").read().split("\n") if number
    ]
    result = three_sum(numbers)

    print(result)
