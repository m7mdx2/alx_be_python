class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Static methods do not access class or instance-specific data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Class methods can access class-specific attributes.
        """
        # Accessing the class attribute using cls
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
