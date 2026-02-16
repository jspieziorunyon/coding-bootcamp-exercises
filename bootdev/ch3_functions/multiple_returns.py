"""
Complete the become_warrior function. It accepts 2 inputs:

The full_name string
The power integer
It should return 2 values:

A title string
A new_power integer.
Create the title using f-strings. Combine full_name with "the warrior" in this format:
full_name the warrior
"""
def become_warrior(full_name, power):
    title = f"{full_name} the warrior"
    new_power = power + 1
    return title, new_power


# Don't edit below this line


def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()
