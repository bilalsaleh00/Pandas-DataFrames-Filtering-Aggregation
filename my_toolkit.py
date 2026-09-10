def calculate_average(numbers):
    """Return the average of a list of numbers."""
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


def find_max_and_min(numbers):
    """Return the maximum and minimum values."""
    if len(numbers) == 0:
        return (0, 0)

    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    return (maximum, minimum)


def count_occurrences(items, target):
    """Return how many times target appears in the list."""
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """Return True if the text is a palindrome."""
    text = text.lower()
    text = text.replace(" ", "")

    return text == text[::-1]


def create_report(title, scores):
    """Return a formatted report containing score statistics."""
    average = calculate_average(scores)
    maximum, minimum = find_max_and_min(scores)

    return f"""
{title}
Average: {average:.2f}
Maximum: {maximum}
Minimum: {minimum}
"""


if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))