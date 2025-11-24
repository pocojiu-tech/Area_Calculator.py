while True:
    print('***** Area Calculator *****')
    print("""
Press 1 to calculate area of square.
Press 2 to calculate area of rectangle.
Press 3 to calculate area of triangle.
Press 4 to calculate area of circle.
Press 5 to Exit from Calculator
""")

    choos = int(input('Enter your Number - '))

    if choos == 1:
        num1 = int(input('Enter side of square - '))
        print("Area =", num1 ** 2)

    elif choos == 2:
        length = int(input('Enter the length of rectangle - '))
        width = int(input('Enter the width of rectangle - '))
        print("Area =", length * width)

    elif choos == 3:
        base = int(input('Enter the base of triangle - '))
        height = int(input('Enter the height of triangle - '))
        print("Area =", 0.5 * base * height)

    elif choos == 4:
        radi = int(input('Enter the radius - '))
        print("Area =", 3.14 * radi * radi)

    elif choos == 5:
        print('Thank you for Using the Calculator')
        break

    else:
        print("Invalid choice! Please try again.")
