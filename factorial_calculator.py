"""
Filename: factorial_calculator.py
Author: <Fontaine, Michael>
Created: <3/4/2026>
Instructor: Holtslander
"""

def factorial():
    # Write your code here
    print("Enter a non-negative whole number on the line below.")
    number = input()            
    number = int(number)          
    if number == 0:
        print("0! = 1")
    else:
        total = 1
        answer_string = ""
        i = number
        while i >= 1:
            total = total * i
            if i == 1:
                answer_string = answer_string + str(i)
            else:
                answer_string = answer_string + str(i) + " * "
            i = i - 1
        print(str(number) + "! = " + answer_string + " = " + str(total))
# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()"""
