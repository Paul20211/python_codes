class Temparature:
    def __init__(self, convert_celsius, convert_fahrenheit):
        self.convert_celsius = convert_celsius
        self.convert_fahrenheit = convert_fahrenheit

    def celsius(self):
        return (self.convert_fahrenheit * 1.8) + 32

    def fahrenheit(self):
        return (self.convert_celsius * 1.8) - 32


P1 = Temparature(32, 45)
print(P1.celsius())
print(P1.fahrenheit())
