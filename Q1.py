class Calculator:
    #constructor to set current calculator value
    #initialized to 0
    def __init__(self):
        self.value = 0

    #add two values, set current calculator value
    def adder(self, input1, input2):
        self.value = input1 + input2

    #subtract two values, set current calculator value
    def subtracter(self, input1, input2):
        self.value = input1 - input2

    #multiply two values, set current calculator value
    def multiplier(self, input1, input2):
        self.value = input1 * input2

    #divide two values, set current calculator value
    def divider(self, input1, input2):
        self.value = input1 / input2

    #reset current calculator value to 0
    def clear(self):
        self.value = 0

# create calculator object
c = Calculator()

#get two values to perform all operations
input1 = input("Enter your input 1: ")
input2 = input("Enter your input 2: ")

input1 = int(input1)
input2 = int(input2)

c.adder(input1, input2)
print(c.value)

c.subtracter(input1, input2)
print(c.value)

c.multiplier(input1, input2)
print(c.value)

c.divider(input1, input2)
print(c.value)

c.clear()
print(c.value)