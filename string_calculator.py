import logging
import re


class StringCalculator:

    def __init__(self, delimiter: str = ","):
        self.default_delimiter = delimiter

        # Simplified logging setup
        logging.basicConfig(
            filename='string_calc.log',
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger()

    @staticmethod
    def get_numbers(nums):

        matches = re.findall(r'-?\d+', nums)
        return matches

    def add(self, numbers: str) -> int:
        self.logger.info(f"Input: {numbers}")

        if not numbers:
            result = 0
            self.logger.info(f"Output: {result}")
            return result

        matches = StringCalculator.get_numbers(numbers)
        negatives = []
        total = 0
        for element in matches:
            if int(element) < 0:
                negatives.append(element)
            if int(element) <= 1000:
                total += int(element)

        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
        return total


if __name__ == "__main__":
    calc = StringCalculator()
    print(calc.add("1000,1001,2"))  # Output: 2003
    print(calc.add("1\n2,3,4"))  # Output: 10
    print(calc.add("//;\n1;2;3;4"))  # Output: 10
    print(calc.add("1,2,-3,4,-5"))
