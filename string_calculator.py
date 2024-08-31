class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Check for custom delimiter
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)
        else:
            delimiter = ","

        # Replace newlines with the delimiter and split the string
        numbers = numbers.replace("\n", delimiter)
        num_list = [int(num) for num in numbers.split(delimiter) if num]

        # Filter out numbers greater than 1000
        num_list = [num for num in num_list if num <= 1000]

        # Check for negative numbers
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

        return sum(num_list)
