#!/usr/bin/env python
# Created By: Chanella
# Date: March fri, 21
# Modified by : March 21 2025
# This program checks if there is over 30 students
import constants

def main():

    # input
    number_of_students = int(input("Enter the number of students: "))
    print("")

    # process & output
    if number_of_students == constants.MAX_STUDENTS:
        print("Exactly {} students.".format(constants.MAX_STUDENTS))
    else:
        print("Not {}students.".format(constants.MAX_STUDENTS))

        if __name__ == "__main__":
           main()
