# Beginner Python Project: Add Two Numbers

This project is a simple Python program for beginners.
It asks the user for **two numbers** and prints their **sum**.

## How to run

From the repository root, run:

```bash
python3 beginner_sum_project/app.py
```

Then enter two numbers when asked.

## Step-by-step code explanation

### 1) `float(input("Enter the first number: "))`
- `input(...)` shows a message and waits for what the user types.
- What the user types is text (a string) at first.
- `float(...)` converts that text to a number so we can do math.

### 2) `float(input("Enter the second number: "))`
- This does the same thing for the second number.

### 3) `sum_result = first_number + second_number`
- `+` adds the two numbers.
- The result is stored in `sum_result`.

### 4) `print(f"The sum is: {sum_result}")`
- `print(...)` displays text in the terminal.
- `f"..."` is an f-string, which lets us insert variable values directly.

## Example

If you enter:
- first number: `5`
- second number: `7`

Output:

```text
The sum is: 12.0
```
