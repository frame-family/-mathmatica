
        #mathmatic formulas
        #by Dave Frame
    def rect_area:

        correct_input = True                #function to figure area of rectangle
        while correct_input:                #loop to assure proper input
    
            try:
                length = float(input("enter length of one side: "))     #enter length
                width = float(input("enter length of other side: "))    #enter second side
                area = length * width                                   #does math
            
            except ValueError:              #checks for proper answer-requests proper input
                print('  Please make sure you enter valid integers for both sides')

            else:
                correct_input = False       #when input correct prints solution to screen
                print('The area of a rectangle', length,'by', width,'is', area,)


    def triang_area:

        correct_input = True
        while correct_input:

            try:
               side1 = float(input("enter length of side adjacent to 90 degree angle"))
                side2 = float(input("enter length of other adjacent side"))

            except ValueError:
                print("please make sure you enter valid intergers for both sides")

            else:
                correct_input = False
                print ("The area of a triangle", side1, "by", side2, "is", side1*side2/2,)
                

    def circle_area:

        correct_input = True
        while correct_input:

            try:

    def circle_circum:

        correct_input = True
        while correct_input:

            try:
                radius = float(input("enter radius of circle"))

            except ValueError:
                print ("please make sure you enter valid intergers for radius")

            else:
                correct_input = False
                print ("The area of the circle with a radius of:", radius*3.14,)

if __name__=='__main__':                     #Program starts here
    correct_input = True
    while correct_input:

        try:
            a = 0
            problem = a(input("Please enter the number"/n"for the problem you want to figure:"/n"1.   Area of a Rectangle,"/n"2.   Area of a Triangle,"/n
                          "3.   Area of a Circle."/n"4.  Circumference of a Circle"/n"Enter 'q' to quit.))
            if problem == 1:
                rect_area
            elif problem == 2:
                triang_area
            elif problem == 3:
                circle_area
            elif problem == 4:
                circle_circum
            elif problem == q:
                quit 



              
              
