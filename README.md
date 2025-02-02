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
**Usage**
Save the calculator python file and run it. 
Entering Expressions:
Type your mathematical expression in the entry box.
The calculator accepts input via both buttons and keyboard.
Special handling:
Use |...| for absolute value.
Typing 123! automatically converts to factorial(123).
Use x or * for multiplication.
Use ^ for exponentiation (which is converted to Python’s **).
Using Mode Toggles:

**Fraction/Decimal**: Press the "Frac/Dec" button to toggle between fraction and decimal output.
π Format: Press the "Show π" button to toggle π formatting. When ON, numbers nearly equal to an integer multiple of π are shown in terms of π.
Trigonometric Mode: Press the "Deg/Rad" button to toggle between Degrees and Radians. The bottom panel updates to reflect the current mode.
Advanced Operations:

**Euler’s Totient Function (φ)**: Located in Row 4, Column 5.
Prime Count: Located in Row 7, Column 4 (labeled "prime#") shows the number of primes ≤ the entered number.
Cubic Root: The "∛" button in Row 7, Column 4 inserts cbrt( so you can calculate the cubic root.
Floor/Ceiling: Buttons in Row 8 apply floor and ceiling operations directly.
Factorial: The "!" button in Row 8 inserts an exclamation mark; when placed after a number (e.g., 5!), it is interpreted as the factorial.
Calculation History:

The history panel displays your past calculations.
Each entry includes the expression and its result.
Use the "X" next to each entry to delete that calculation.
Click "Clear History" to remove all entries.
Customization
You can modify the button labels, sizes, fonts, or other settings by editing the code. The mode toggles and evaluation preprocessing are implemented in the helper functions, making further customization straightforward.

**License**
This project is provided "as is" without warranty. Feel free to modify and use it as needed.
