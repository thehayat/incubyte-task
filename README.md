# String Calculator TDD Kata

This project implements a simple string calculator in Python using Test-Driven Development (TDD) principles. The
calculator takes a string of numbers and returns their sum, supporting various delimiters, including custom ones, and
handling edge cases such as empty strings and negative numbers.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Tests](#tests)
- [Streamlit App](#streamlit-app)

## Getting Started

### Prerequisites Used

- Python 3.9
- `pytest` for running tests
- `streamlit` for the web app

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/thehayat/incubyte-task.git
    ```

2. Navigate to the project directory:

    ```bash
    cd incubyte-task
    ```

3. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the string calculator, simply import the `add` function and pass a string of numbers:

```python
from string_calculator import StringCalculator

calculator = StringCalculator()
result = calculator.add("1,2,3")
print(result)  # Output: 6
```
## Tests
Run the tests with PyTest

 ```bash
 python test_string_calculator.py
 ```


## Streamlit-app

Run the streamlit App:

 ```bash
 streamlit run app.py
 ```
