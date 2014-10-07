#Stephen Snow
#07/10/2014
#Grade boundary

grade_number = int(input("Please enter the grade you scored in the exam:"))
if grade_number >= 81:
    print ("Grade A")
elif grade_number >=71:
    print ("Grade B")
elif grade_number >=61:
    print ("Grade C")
elif grade_number >=51:
    print ("Grade D")
elif grade_number >=41:
     print ("Grade E")
elif grade_number <41:
    print ("Grade U")
else:
    print("This mark does not relate to any existing Grade")
    

