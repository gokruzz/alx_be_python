# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Add two numbers without using class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Multiply two numbers and access a class-level attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
