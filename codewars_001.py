def narcissistic(value: int):
    digits = [int(num) for num in str(value)]
    n = len(digits)
    if len(str(value)) == 1:
        return True
    elif sum([num ** n for num in digits]) == value:
        return True
    else:
        return False


print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def dirReduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []
    for direction in arr:
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))  # Output: ['WEST']
print(dirReduc(["NORTH", "SOUTH", "EAST", "WEST"]))  # Output: []
print(dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]))  # Output: ['WEST', 'WEST']


def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        spaces = " " * (n_floors - i - 1)
        stars = "*" * (2 * i + 1)
        tower.append(spaces + stars + spaces)
    return tower


print(tower_builder(3))
print(tower_builder(6))

def sequence_classifier(arr):
    if all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)):
        return 1
    elif all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return 2
    elif all(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        return 3
    elif all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return 4
    elif all(arr[i] == arr[i + 1] for i in range(len(arr) - 1)):
        return 5
    else:
        return 0

def format_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(format_time(3661))  # Output: '01:01:01'


