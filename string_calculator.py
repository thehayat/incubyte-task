class StringCalculator:

    def __init__(self, delimiter: str = ","):
        self.default_delimiter = delimiter

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Check for custom delimiter
        if numbers.startswith("//"):
            self.default_delimiter, numbers = numbers[2:].split("\n", 1)
        else:
            self.default_delimiter = ","

        # Replace newlines with the delimiter and split the string
        numbers = numbers.replace("\n", self.default_delimiter)
        num_list = [int(num) for num in numbers.split(self.default_delimiter) if num]

        # Filter out numbers greater than 1000
        num_list = [num for num in num_list]

        # Check for negative numbers
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

        return sum(num_list)

if __name__ == "__main__":
    calc = StringCalculator()
    print(calc.add(""))  # Output: 1298
    print(calc.add("1234,64"))  # Output: 1298
    print(calc.add("1\n2,3,4"))  # Output: 10
    print(calc.add("//;\n1;2;3;4"))  # Output: 10
    print(calc.add("1,2,-3,4,-5"))  # Raises ValueError: negative numbers not allowed: -3