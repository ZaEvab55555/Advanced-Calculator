"""
Advanced Calculator
===================
A feature-rich calculator with:

- Basic arithmetic and advanced operations.
- Additional functions: Euler's totient (φ), prime count, cubic root, floor, ceiling.
- Mode toggles for Fraction/Decimal, π formatting (only for values nearly exactly an integer multiple of π), and Trigonometric (Degrees/Radians).
- Recognizes "x" as multiplication and supports absolute value notation using |...|.
- A scrollable calculation history panel on the right that shows each calculation 
  (operation and result in different fonts), with individual delete buttons and a 
  new "Copy" button next to the answer.
- Buttons arranged in 8 full rows (6 buttons per row) and a bottom panel showing current modes.
- Specific replacements:
    • Row 4, Column 5: φ button computes Euler’s totient function.
    • Row 7, Column 4: "prime#" button counts the number of primes ≤ the entered number.
    • Row 7, Column 5: The "∛" button inserts "cbrt(" into the entry.
    • Row 8, Column 3: "Deg/Rad" toggles between degree and radian mode (in sync with the bottom panel).
    • Floor and ceiling buttons in Row 8 apply floor/ceil rounding directly.
    • The factorial button ("!") in Row 8 inserts "!" so that expressions like "123!" are interpreted as factorial(123).
- The safe evaluation function pre-processes the expression (handling '^', 'x', |...|, etc.).
- Floating-point results are rounded (to 10 decimal places) to avoid glitches.
- In π mode, only values that are nearly exactly integer multiples of π (tolerance 1e-10) are formatted.
- All buttons and the window are wider.
"""

import tkinter as tk
from tkinter import messagebox
import math
from fractions import Fraction
import re

# ----------------------------------------------------------------------
# Additional Math Functions
# ----------------------------------------------------------------------
def totient(n):
    """Compute Euler's totient function for n."""
    if n <= 0:
        return 0
    result = n
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result

def prime_count(n):
    """Count the number of prime numbers ≤ n using a simple sieve."""
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sum(sieve)

def cubic_root(x):
    """Compute the real cubic root of x."""
    return x ** (1/3) if x >= 0 else -((-x) ** (1/3))

# Alias for convenience
def cbrt(x):
    return cubic_root(x)

# ----------------------------------------------------------------------
# Global Mode Flags
# ----------------------------------------------------------------------
# trig_mode: False means Degrees (default), True means Radians.
# fraction_mode: False means Decimal (default), True means Fraction.
# pi_mode: True means use π formatting (only when result is nearly an integer multiple of π, tolerance 1e-10); False means show exact.
trig_mode = False
fraction_mode = False
pi_mode = True

# ----------------------------------------------------------------------
# Helper Functions for Evaluation and Conversion
# ----------------------------------------------------------------------
def safe_eval(expression):
    """
    Evaluate the expression safely after preprocessing:
      - Replace '^' with '**'
      - Replace 'x' with '*' for multiplication
      - Replace any inserted 'π' with math.pi
      - Convert patterns like "123!" into "factorial(123)"
      - Convert |...| into abs(...)
    """
    expression = expression.replace('^', '**')
    expression = expression.replace('x', '*')
    expression = expression.replace('π', str(math.pi))
    expression = re.sub(r'\|([^|]+)\|', r'abs(\1)', expression)
    expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)
    try:
        result = eval(expression, {"__builtins__": None}, {
            'sin': math.sin if trig_mode else lambda x: math.sin(math.radians(x)),
            'cos': math.cos if trig_mode else lambda x: math.cos(math.radians(x)),
            'tan': math.tan if trig_mode else lambda x: math.tan(math.radians(x)),
            'asin': math.asin if trig_mode else lambda x: math.degrees(math.asin(x)),
            'acos': math.acos if trig_mode else lambda x: math.degrees(math.acos(x)),
            'atan': math.atan if trig_mode else lambda x: math.degrees(math.atan(x)),
            'sqrt': math.sqrt,
            'log': math.log,
            'ln': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'floor': math.floor,
            'ceil': math.ceil,
            'factorial': math.factorial,
            'cbrt': cbrt,
            'pi': math.pi,
            'e': math.e,
            'abs': abs
        })
        return result
    except Exception as e:
        raise e

def convert_to_scientific(num):
    """Convert a number to scientific notation: <mantissa> x 10^<exponent>."""
    try:
        s = format(num, ".6e")
        mantissa, exp_part = s.split("e")
        exponent = int(exp_part)
        return f"{mantissa} x 10^{exponent}"
    except Exception:
        return str(num)

def convert_to_pi_format(result):
    """
    If result is a float and is nearly equal to an integer multiple of π 
    (with tolerance 1e-10), return a string like "π", "2π", "-π", etc.
    Otherwise, return the exact result as a string.
    """
    if isinstance(result, float):
        factor = round(result / math.pi)
        if abs(result - factor * math.pi) < 1e-10:
            if factor == 1:
                return "π"
            elif factor == -1:
                return "-π"
            else:
                return f"{factor}π"
    return str(result)

# ----------------------------------------------------------------------
# Calculator Operation Functions
# ----------------------------------------------------------------------
def totient_action():
    try:
        n = int(entry.get())
        result = totient(n)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid input for totient function")

def prime_count_action():
    try:
        n = int(entry.get())
        result = prime_count(n)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid input for prime count")

def square_value():
    try:
        value = float(entry.get())
        result = value ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid input for squaring")

def reciprocal_value():
    try:
        value = float(entry.get())
        if value == 0:
            raise ZeroDivisionError
        result = 1 / value
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid input for reciprocal (division by zero?)")

def prime_factorization():
    try:
        n = int(entry.get())
        if n < 0:
            n = -n
        if n < 2:
            result = str(n)
        else:
            factors = {}
            temp = n
            p = 2
            while p * p <= temp:
                while temp % p == 0:
                    factors[p] = factors.get(p, 0) + 1
                    temp //= p
                p += 1
            if temp > 1:
                factors[temp] = factors.get(temp, 0) + 1
            parts = []
            for prime in sorted(factors.keys()):
                if factors[prime] == 1:
                    parts.append(str(prime))
                else:
                    parts.append(f"{prime}^{factors[prime]}")
            result = " x ".join(parts)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Enter a valid integer for factorization")

# ----------------------------------------------------------------------
# Mode Toggle Functions
# ----------------------------------------------------------------------
def toggle_fraction_mode():
    global fraction_mode
    fraction_mode = not fraction_mode
    fraction_label.config(text="Fraction" if fraction_mode else "Decimal")
    try:
        num = float(entry.get())
        if fraction_mode:
            frac = Fraction(num).limit_denominator(1000)
            entry.delete(0, tk.END)
            entry.insert(tk.END, frac)
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, num)
    except Exception:
        pass

def toggle_trig_mode():
    global trig_mode
    trig_mode = not trig_mode
    trig_label.config(text="Radians" if trig_mode else "Degrees")

def toggle_pi_mode():
    global pi_mode
    pi_mode = not pi_mode
    pi_label.config(text="π" if pi_mode else "Exact")

# ----------------------------------------------------------------------
# Button Insertion & Evaluation Functions
# ----------------------------------------------------------------------
def button_action(value):
    entry.insert(tk.END, value)

def evaluate_expression():
    try:
        expr = entry.get()
        result = safe_eval(expr)
        if isinstance(result, float):
            result = round(result, 10)
        if fraction_mode:
            result = Fraction(result).limit_denominator(1000)
        elif pi_mode:
            result = convert_to_pi_format(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        add_history(expr, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        print(e)

def convert_sci_notation_action():
    try:
        value = float(entry.get())
        sci = convert_to_scientific(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, sci)
    except Exception:
        messagebox.showerror("Error", "Invalid input for SCI conversion")

def delete_last():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)

def clear_entry():
    entry.delete(0, tk.END)

# Additional functions for new buttons:
def insert_pi():
    entry.insert(tk.END, "π")

def insert_cbrt():
    entry.insert(tk.END, "cbrt(")

def convert_rad_to_deg():
    try:
        value = float(entry.get())
        result = math.degrees(value)
        if pi_mode:
            result = convert_to_pi_format(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid input for Rad→Deg conversion")

def convert_deg_to_rad():
    try:
        value = float(entry.get())
        result = math.radians(value)
        if pi_mode:
            result = convert_to_pi_format(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid input for Deg→Rad conversion")

def apply_floor():
    try:
        value = float(entry.get())
        result = math.floor(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid input for floor")

def apply_ceil():
    try:
        value = float(entry.get())
        result = math.ceil(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid input for ceiling")

# ----------------------------------------------------------------------
# History Panel Functions
# ----------------------------------------------------------------------
def add_history(operation, solution):
    """
    Adds a calculation entry to the history panel.
    Each entry is a frame that fills the width of the history panel.
    It displays:
      - The operation on top (centered, Courier New 16 bold)
      - The solution below (centered, Courier New 16 italic)
      - A "Copy" button next to the solution to copy the answer
      - A delete button ("X") to remove the entry.
    """
    def copy_answer():
        root.clipboard_clear()
        root.clipboard_append(str(solution))
    
    hist_frame = tk.Frame(history_frame, bd=1, relief="solid", padx=5, pady=5)
    op_label = tk.Label(hist_frame, text=operation, font=("Courier New", 16, "bold"),
                        anchor="center", justify="center")
    sol_label = tk.Label(hist_frame, text=solution, font=("Courier New", 16, "italic"),
                         fg="blue", anchor="center", justify="center")
    copy_btn = tk.Button(hist_frame, text="Copy", font=("Courier New", 12), command=copy_answer)
    del_btn = tk.Button(hist_frame, text="X", font=("Courier New", 12), command=lambda: hist_frame.destroy())
    
    # Arrange: operation spans full width in row 0.
    op_label.grid(row=0, column=0, columnspan=3, sticky="ew")
    # In row 1, put solution, copy, and delete buttons.
    sol_label.grid(row=1, column=0, sticky="ew")
    copy_btn.grid(row=1, column=1, padx=5)
    del_btn.grid(row=1, column=2, padx=5)
    hist_frame.grid_columnconfigure(0, weight=1)
    hist_frame.pack(fill="x", padx=5, pady=2)

def clear_history():
    for child in history_frame.winfo_children():
        child.destroy()

# ----------------------------------------------------------------------
# Main GUI Setup
# ----------------------------------------------------------------------
root = tk.Tk()
root.title("Advanced Calculator")
root.minsize(width=1000, height=600)

# Entry (Answer) Box (centered) - increased width
entry = tk.Entry(root, font=("Arial", 18), justify="center", width=35, bd=5, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

# ----------------------------------------------------------------------
# Calculator Buttons Layout (8 rows, 6 columns)
# ----------------------------------------------------------------------
default_color = "#add8e6"
button_width = 8

# Rows 1–7: Original Buttons
button_specs = [
    # Row 1
    (1, 0, '7', lambda: button_action('7')),
    (1, 1, '8', lambda: button_action('8')),
    (1, 2, '9', lambda: button_action('9')),
    (1, 3, '/', lambda: button_action('/')),
    (1, 4, '^', lambda: button_action('^')),
    (1, 5, 'DEL', lambda: delete_last(), "#ffcccc"),
    
    # Row 2
    (2, 0, '4', lambda: button_action('4')),
    (2, 1, '5', lambda: button_action('5')),
    (2, 2, '6', lambda: button_action('6')),
    (2, 3, '*', lambda: button_action('*')),
    (2, 4, '√', lambda: button_action('sqrt(')),
    (2, 5, 'C', lambda: clear_entry(), "#ff6666"),
    
    # Row 3
    (3, 0, '1', lambda: button_action('1')),
    (3, 1, '2', lambda: button_action('2')),
    (3, 2, '3', lambda: button_action('3')),
    (3, 3, '-', lambda: button_action('-')),
    (3, 4, '(', lambda: button_action('(')),
    (3, 5, ')', lambda: button_action(')')),
    
    # Row 4
    (4, 0, '0', lambda: button_action('0')),
    (4, 1, '.', lambda: button_action('.')),
    (4, 2, '±', lambda: button_action('±')),
    (4, 3, '+', lambda: button_action('+')),
    (4, 4, 'φ', totient_action),
    (4, 5, 'SCI', convert_sci_notation_action),
    
    # Row 5
    (5, 0, 'sin', lambda: button_action('sin(')),
    (5, 1, 'cos', lambda: button_action('cos(')),
    (5, 2, 'tan', lambda: button_action('tan(')),
    (5, 3, 'asin', lambda: button_action('asin(')),
    (5, 4, 'acos', lambda: button_action('acos(')),
    (5, 5, 'atan', lambda: button_action('atan(')),
    
    # Row 6
    (6, 0, 'log', lambda: button_action('log(')),
    (6, 1, 'ln', lambda: button_action('ln(')),
    (6, 2, 'Prime', prime_factorization),
    (6, 3, 'x²', square_value),
    (6, 4, '1/x', reciprocal_value),
    (6, 5, 'Frac/Dec', toggle_fraction_mode),
    
    # Row 7
    (7, 0, 'π', insert_pi),
    (7, 1, 'Rad→Deg', convert_rad_to_deg),
    (7, 2, 'Deg→Rad', convert_deg_to_rad),
    (7, 3, 'prime#', prime_count_action),
    (7, 4, '∛', insert_cbrt),
    (7, 5, 'mod', lambda: button_action('%'))
]

# Row 8: PI Format Toggle and Extra Operations
new_button_specs = [
    (8, 0, 'Show π', toggle_pi_mode),
    (8, 1, '!', lambda: button_action('!')),
    (8, 2, 'abs', lambda: button_action('abs(')),
    (8, 3, 'Deg/Rad', toggle_trig_mode),
    (8, 4, 'floor', apply_floor),
    (8, 5, 'ceil', apply_ceil)
]

all_buttons = button_specs + new_button_specs

for spec in all_buttons:
    if len(spec) == 5:
        r, c, text, cmd, bg = spec
    else:
        r, c, text, cmd = spec
        bg = default_color
    btn = tk.Button(root, text=text, font=("Arial", 14), width=button_width, height=2, command=cmd, bg=bg)
    btn.grid(row=r, column=c, padx=3, pady=3)

# ----------------------------------------------------------------------
# History Panel (Right Side)
# ----------------------------------------------------------------------
history_panel = tk.Frame(root, bd=2, relief="groove")
history_panel.grid(row=0, column=6, rowspan=10, sticky="nsw", padx=5, pady=5)

clear_history_btn = tk.Button(history_panel, text="Clear History", font=("Courier New", 12), command=clear_history)
clear_history_btn.pack(fill="x", padx=5, pady=5)

history_canvas = tk.Canvas(history_panel, width=300, height=500)
history_scrollbar = tk.Scrollbar(history_panel, orient="vertical", command=history_canvas.yview)
history_canvas.configure(yscrollcommand=history_scrollbar.set)
history_scrollbar.pack(side="right", fill="y")
history_canvas.pack(side="left", fill="both", expand=True)

history_frame = tk.Frame(history_canvas)
history_canvas.create_window((0, 0), window=history_frame, anchor="nw")

def on_history_configure(event):
    history_canvas.configure(scrollregion=history_canvas.bbox("all"))
history_frame.bind("<Configure>", on_history_configure)

def clear_history():
    for child in history_frame.winfo_children():
        child.destroy()

# ----------------------------------------------------------------------
# Bottom Panel (Row 9)
# ----------------------------------------------------------------------
bottom_frame = tk.Frame(root)
bottom_frame.grid(row=9, column=0, columnspan=6, sticky="we", padx=5, pady=5)
bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=1)
bottom_frame.columnconfigure(2, weight=1)

fraction_label = tk.Label(bottom_frame, text="Decimal", font=("Arial", 12))
fraction_label.grid(row=0, column=0, sticky="w")

pi_label = tk.Label(bottom_frame, text="π" if pi_mode else "Exact", font=("Arial", 12))
pi_label.grid(row=0, column=1)

trig_label = tk.Label(bottom_frame, text="Degrees", font=("Arial", 12))
trig_label.grid(row=0, column=2, sticky="e")

# ----------------------------------------------------------------------
# Bind Enter key to evaluate the expression
# ----------------------------------------------------------------------
root.bind('<Return>', lambda event: evaluate_expression())

# ----------------------------------------------------------------------
# Run the Application
# ----------------------------------------------------------------------
root.mainloop()
