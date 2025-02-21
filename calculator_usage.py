from main import Calculator
import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        
        # Style
        self.root.configure(bg='#f0f0f0')
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TLabel', padding=5)
        
        # Input frames
        input_frame = ttk.Frame(root, padding="10")
        input_frame.pack(fill='x', padx=10, pady=5)
        
        # Number inputs
        ttk.Label(input_frame, text="First Number:").pack()
        self.num1 = ttk.Entry(input_frame)
        self.num1.pack(fill='x', pady=5)
        
        ttk.Label(input_frame, text="Second Number:").pack()
        self.num2 = ttk.Entry(input_frame)
        self.num2.pack(fill='x', pady=5)
        
        # Notebook for different operation categories
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Basic Operations Tab
        basic_frame = ttk.Frame(self.notebook)
        self.notebook.add(basic_frame, text='Basic')
        self.create_basic_operations(basic_frame)
        
        # Advanced Operations Tab
        advanced_frame = ttk.Frame(self.notebook)
        self.notebook.add(advanced_frame, text='Advanced')
        self.create_advanced_operations(advanced_frame)
        
        # Trigonometric Operations Tab
        trig_frame = ttk.Frame(self.notebook)
        self.notebook.add(trig_frame, text='Trigonometric')
        self.create_trigonometric_operations(trig_frame)
        
        # Result display
        self.result_var = tk.StringVar()
        result_label = ttk.Label(root, textvariable=self.result_var, wraplength=350)
        result_label.pack(pady=10)

    def get_numbers(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            return Calculator(num1, num2)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
            return None

    def create_basic_operations(self, parent):
        operations = [
            ('Addition', 'add'),
            ('Subtraction', 'subtract'),
            ('Multiplication', 'multiply'),
            ('Division', 'divide'),
            ('Power', 'power'),
            ('Modulus', 'modulus')
        ]
        
        for text, operation in operations:
            btn = ttk.Button(parent, text=text,
                           command=lambda op=operation: self.calculate(op))
            btn.pack(fill='x', pady=2, padx=5)

    def create_advanced_operations(self, parent):
        operations = [
            ('Square Root (First Number)', 'square_root'),
            ('Factorial (First Number)', 'factorial'),
            ('Logarithm', 'log')
        ]
        
        for text, operation in operations:
            btn = ttk.Button(parent, text=text,
                           command=lambda op=operation: self.calculate(op))
            btn.pack(fill='x', pady=2, padx=5)

    def create_trigonometric_operations(self, parent):
        operations = [
            ('Sine (First Number)', 'sin'),
            ('Cosine (First Number)', 'cos'),
            ('Tangent (First Number)', 'tan')
        ]
        
        for text, operation in operations:
            btn = ttk.Button(parent, text=text,
                           command=lambda op=operation: self.calculate(op))
            btn.pack(fill='x', pady=2, padx=5)

    def calculate(self, operation):
        calc = self.get_numbers()
        if calc:
            try:
                result = getattr(calc, operation)()
                self.result_var.set(f"Result: {result}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 