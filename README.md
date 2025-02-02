The Advanced Calculator is a feature-rich Python-based calculator that supports both basic arithmetic and advanced mathematical operations. It offers an intuitive user interface with extensive functionality, including mode toggles, expression parsing enhancements, and a scrollable calculation history panel.

Features
Basic Operations:

Addition, subtraction, multiplication, and division.
Exponentiation (using ^ or the letter x as multiplication).
Advanced Mathematical Functions:

Square root (√)
Euler’s Totient Function (φ): Calculates the number of positive integers up to n that are relatively prime to n.
Prime Factorization: Displays the prime factors of a number (e.g., 24 → 2^3 x 3).
Prime Counting: Counts the number of primes less than or equal to a given number.
Cubic Root: Inserts cbrt( into the expression for calculating the real cubic root.
Floor and Ceiling: Buttons that directly apply floor and ceiling rounding to the current number.
Absolute Value: Supports the use of the pipe symbol (|...|) to calculate the absolute value.
Factorial: Recognizes patterns like 123! and converts them to factorial(123).
Scientific Notation: Convert numbers to scientific notation format (e.g., 1.234560 x 10^2).
Trigonometric Functions:

Standard functions: sin, cos, tan.
Inverse functions: asin, acos, atan.
Mode toggle for trigonometry: Switch between Degrees and Radians.
Mode Toggles:

Fraction/Decimal Mode: Toggle whether numerical results are displayed as decimals or as fractions.
π Format Mode: Toggle whether results are shown in terms of π (only if they are within a tight tolerance of an integer multiple of π) or in their exact numerical form.
Trigonometric Mode: Toggle between Degrees and Radians.
Expression Preprocessing:

Recognizes both x and * for multiplication.
Converts ^ to ** for exponentiation.
Transforms expressions such as 123! into factorial(123).
Converts absolute value notation using pipes, e.g., | -2 | becomes abs(-2).
Calculation History Panel:

A scrollable panel on the right side displays each calculation.
Each history entry shows:
The operation (displayed in Courier New, 16 bold, centered).
The solution (displayed in Courier New, 16 italic, centered).
Each entry spans the full width of the history panel.
Individual delete buttons ("X") allow for the removal of specific history entries.
A "Clear History" button at the top clears the entire history.
User Interface:

The calculator window and buttons are wide for ease of use.
The answer entry is centered and wide.
A bottom panel shows the current mode settings:
Left: Fraction/Decimal mode.
Center: π format mode.
Right: Trigonometric mode (Degrees/Radians).
Requirements
Python 3.x
Standard Python libraries (tkinter, math, fractions, and re)
No external libraries are required.
