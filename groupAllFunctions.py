class groupAllFunctions():
    def Subfields():
        subfields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for field in subfields:
            print(field)
    
    def OddEven():
        num = int(input('Enter a number: '))
        if(num % 2 == 0):
            print(num, " is Even number")
        else:
            print(num, " is Odd number")

    def Elegible():
        gender = (input("Your Gender: "))
        age = (int(input("Your Age: ")))
        if(gender == 'male'):
            if(age >= 21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            if(age >= 18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
    def percentage():
        sub1 = int(input("Subject1= "))
        sub2 = int(input("Subject2= "))
        sub3 = int(input("Subject3= "))
        sub4 = int(input("Subject4= "))
        sub5 = int(input("Subject5= "))
        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = total / 5
        print("Total : ", total)
        print("Percentage : ", percentage , "%")
    def triangle():
        height = int(input("Height: "))
        breadth = int(input("Breadth: "))
        area = (height * breadth) / 2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: " , area)
        height1 = int(input("Height1: "))
        height2 = int(input("Height2: "))
        breadth = int(input("Breadth: "))
        perimeter = (height1) + (height2) + (breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", perimeter)