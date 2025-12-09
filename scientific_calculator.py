#!/usr/bin/env python3
"""
Scientific Calculator - Python GUI Version
A comprehensive scientific calculator with trigonometric, logarithmic, and other functions.
"""

import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("⚓ Scientific Calculator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Variables
        self.current_input = "0"
        self.memory = 0
        self.expression = ""
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        # Keyboard bindings
        self.setup_keyboard()
    
    def create_display(self):
        # Expression display
        self.expression_var = tk.StringVar(value="")
        expression_frame = tk.Frame(self.root, bg="#1a1a1a")
        expression_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        
        expression_label = tk.Label(
            expression_frame,
            textvariable=self.expression_var,
            bg="#1a1a1a",
            fg="#888888",
            font=("Courier New", 12),
            anchor="e",
            padx=10,
            pady=5
        )
        expression_label.pack(fill=tk.X)
        
        # Main display
        self.display_var = tk.StringVar(value="0")
        display_frame = tk.Frame(self.root, bg="#1a1a1a")
        display_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            bg="#1a1a1a",
            fg="#00ff41",
            font=("Courier New", 32, "bold"),
            anchor="e",
            padx=20,
            pady=20,
            wraplength=460
        )
        display_label.pack(fill=tk.X)
    
    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button configuration
        buttons = [
            # Row 1: Memory and Clear
            [("MC", self.memory_clear, "memory"), ("MR", self.memory_recall, "memory"),
             ("M+", self.memory_add, "memory"), ("M-", self.memory_subtract, "memory"),
             ("C", self.clear_all, "clear")],
            
            # Row 2: Trigonometric functions
            [("sin", lambda: self.append_function("sin("), "function"),
             ("cos", lambda: self.append_function("cos("), "function"),
             ("tan", lambda: self.append_function("tan("), "function"),
             ("log", lambda: self.append_function("log("), "function"),
             ("ln", lambda: self.append_function("ln("), "function")],
            
            # Row 3: Inverse trig and power
            [("asin", lambda: self.append_function("asin("), "function"),
             ("acos", lambda: self.append_function("acos("), "function"),
             ("atan", lambda: self.append_function("atan("), "function"),
             ("x^y", lambda: self.append_operator("^"), "function"),
             ("√", lambda: self.append_function("sqrt("), "function")],
            
            # Row 4: More functions
            [("e^x", lambda: self.append_function("exp("), "function"),
             ("(", lambda: self.append_operator("("), "operator"),
             (")", lambda: self.append_operator(")"), "operator"),
             ("/", lambda: self.append_operator("/"), "operator"),
             ("CE", self.clear_entry, "clear")],
            
            # Row 5: Numbers
            [("7", lambda: self.append_number("7"), "number"),
             ("8", lambda: self.append_number("8"), "number"),
             ("9", lambda: self.append_number("9"), "number"),
             ("×", lambda: self.append_operator("*"), "operator"),
             ("π", lambda: self.append_constant(str(math.pi)), "function")],
            
            # Row 6: Numbers
            [("4", lambda: self.append_number("4"), "number"),
             ("5", lambda: self.append_number("5"), "number"),
             ("6", lambda: self.append_number("6"), "number"),
             ("-", lambda: self.append_operator("-"), "operator"),
             ("e", lambda: self.append_constant(str(math.e)), "function")],
            
            # Row 7: Numbers
            [("1", lambda: self.append_number("1"), "number"),
             ("2", lambda: self.append_number("2"), "number"),
             ("3", lambda: self.append_number("3"), "number"),
             ("+", lambda: self.append_operator("+"), "operator"),
             ("n!", self.factorial, "function")],
            
            # Row 8: Zero and equals
            [("0", lambda: self.append_number("0"), "number", 2),
             (".", self.append_decimal, "number"),
             ("%", lambda: self.append_operator("%"), "operator"),
             ("=", self.calculate, "equals", 2)]
        ]
        
        # Color scheme
        colors = {
            "number": {"bg": "#f0f0f0", "fg": "#333333", "active": "#e0e0e0"},
            "operator": {"bg": "#ff9500", "fg": "white", "active": "#ff8500"},
            "function": {"bg": "#4a90e2", "fg": "white", "active": "#357abd"},
            "clear": {"bg": "#ff3b30", "fg": "white", "active": "#e02e24"},
            "memory": {"bg": "#8e8e93", "fg": "white", "active": "#6e6e73"},
            "equals": {"bg": "#34c759", "fg": "white", "active": "#30b04f"}
        }
        
        # Create buttons
        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(fill=tk.BOTH, expand=True, pady=2)
            
            for button_info in row:
                if len(button_info) == 4:
                    text, command, btn_type, colspan = button_info
                else:
                    text, command, btn_type = button_info
                    colspan = 1
                
                color = colors[btn_type]
                btn = tk.Button(
                    row_frame,
                    text=text,
                    command=command,
                    bg=color["bg"],
                    fg=color["fg"],
                    activebackground=color["active"],
                    activeforeground=color["fg"],
                    font=("Arial", 14, "bold"),
                    relief=tk.RAISED,
                    borderwidth=2,
                    cursor="hand2"
                )
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
    
    def update_display(self):
        self.display_var.set(self.current_input)
    
    def append_number(self, num):
        if self.current_input == "0" or self.current_input == "Error":
            self.current_input = num
        else:
            self.current_input += num
        self.update_display()
    
    def append_decimal(self):
        if self.current_input == "Error":
            self.current_input = "0."
        elif "." not in self.current_input:
            self.current_input += "."
        self.update_display()
    
    def append_operator(self, op):
        if self.current_input == "Error":
            self.current_input = "0"
        
        last_char = self.current_input[-1] if self.current_input else ""
        if last_char in "+-*/%^":
            self.current_input = self.current_input[:-1] + op
        else:
            self.current_input += op
        self.update_display()
    
    def append_function(self, func):
        if self.current_input == "0" or self.current_input == "Error":
            self.current_input = func
        else:
            last_char = self.current_input[-1] if self.current_input else ""
            if last_char not in "+-*/%^().":
                self.current_input += "*" + func
            else:
                self.current_input += func
        self.update_display()
    
    def append_constant(self, value):
        if self.current_input == "0" or self.current_input == "Error":
            self.current_input = value
        else:
            last_char = self.current_input[-1] if self.current_input else ""
            if last_char not in "+-*/%^().":
                self.current_input += "*" + value
            else:
                self.current_input += value
        self.update_display()
    
    def factorial(self):
        try:
            num = float(self.current_input)
            if num < 0 or not num.is_integer():
                self.current_input = "Error"
                self.update_display()
                return
            
            result = 1
            for i in range(2, int(num) + 1):
                result *= i
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()
    
    def calculate(self):
        try:
            self.expression_var.set(self.current_input)
            
            # Replace function names with math functions
            expression = self.current_input
            expression = expression.replace("sin(", "math.sin(")
            expression = expression.replace("cos(", "math.cos(")
            expression = expression.replace("tan(", "math.tan(")
            expression = expression.replace("asin(", "math.asin(")
            expression = expression.replace("acos(", "math.acos(")
            expression = expression.replace("atan(", "math.atan(")
            expression = expression.replace("log(", "math.log10(")
            expression = expression.replace("ln(", "math.log(")
            expression = expression.replace("exp(", "math.exp(")
            expression = expression.replace("sqrt(", "math.sqrt(")
            expression = expression.replace("^", "**")
            expression = expression.replace("%", "/100")
            
            # Evaluate
            result = eval(expression, {"__builtins__": {}}, {"math": math})
            
            # Format result
            if abs(result) > 1e15 or (abs(result) < 1e-10 and result != 0):
                self.current_input = f"{result:.6e}"
            else:
                result = round(result, 10)
                self.current_input = str(result)
            
            self.update_display()
        except Exception as e:
            self.current_input = "Error"
            self.update_display()
    
    def clear_all(self):
        self.current_input = "0"
        self.expression_var.set("")
        self.update_display()
    
    def clear_entry(self):
        self.current_input = "0"
        self.update_display()
    
    def memory_clear(self):
        self.memory = 0
    
    def memory_recall(self):
        self.current_input = str(self.memory)
        self.update_display()
    
    def memory_add(self):
        try:
            value = float(self.current_input)
            self.memory += value
        except:
            pass
    
    def memory_subtract(self):
        try:
            value = float(self.current_input)
            self.memory -= value
        except:
            pass
    
    def setup_keyboard(self):
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
    
    def on_key_press(self, event):
        key = event.char
        
        if key.isdigit():
            self.append_number(key)
        elif key == '.':
            self.append_decimal()
        elif key in '+-*/':
            self.append_operator(key)
        elif key == '\r' or key == '=':
            self.calculate()
        elif key == '\x1b' or key.lower() == 'c':
            self.clear_all()
        elif key == '(':
            self.append_operator('(')
        elif key == ')':
            self.append_operator(')')
        elif event.keysym == 'BackSpace':
            if len(self.current_input) > 1:
                self.current_input = self.current_input[:-1]
            else:
                self.current_input = "0"
            self.update_display()

def main():
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()