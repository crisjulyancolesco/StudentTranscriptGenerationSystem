# This work done by Group 10:
# Barredo, Harold Wendell E., 2021-04990-MN-0, (30%)
# Gonzales, John Louie, 2021-12084-MN-0, (15%)
# Olesco, Cris Julyan C., 2021-05796-MN-0, (30%)
# Samson, Trixie B., 2021-05805-MN-0, (25%)

import os
import statistics as st
import csv
import pandas as pd
import time as time
import time
from datetime import date
from datetime import datetime

DateToday = date.today()
DateToday = DateToday.strftime("%m/%d/%y")
TimeNow = datetime.now()
TimeNow = TimeNow.strftime("%H:%M:%p")

# Function for the start feauture.
def startFeature():
    # Print the selection for the student level and ask the user.
    print("Select student level: Undergraduate", '\033[1m' + '(U)' + '\033[0m' + ",", "Graduate", '\033[1m' + '(G)' + '\033[0m' + ",", "Both", '\033[1m' + '(B)' + '\033[0m')
    student_level = input("Student Level: ").upper()
    print('')
    count = 0

    # Checks if the user select Graduate or Both
    if student_level == "G" or student_level == "B":
        # Print the selection for the degree and ask the user.
        print("Select Degree: Master", '\033[1m' + '(M)' + '\033[0m' + ",", "Doctorate", '\033[1m' + '(D)' + '\033[0m' + ",", "Both", '\033[1m' + '(B0)' + '\033[0m')
        _degree = input("Degree: ").upper()
    else:
        _degree = None
    
    # Ask the user for the Student ID
    stdID = (input("Enter student ID" + ' ' + '\033[1m' + '(stdID): ' + '\033[0m'))
    
    # Open the studentDetails.csv
    studentDetails = open('studentDetails.csv')
    sdtDetails = csv.reader(studentDetails)
    heading = next(sdtDetails)
    students_ID = []
    # For loop that stores the student ID in a list.
    for row in sdtDetails:
        students_ID.append(row[1])
    
    # Check if the Student ID is valid.
    while stdID not in students_ID:
        stdID = (input("Invalid student ID, Enter student ID" + ' ' + '\033[1m' + '(stdID): ' + '\033[0m'))
  
    time.sleep(3)
    # Calls menu feature with argument input by the user.
    menuFeature(stdID, student_level, _degree, count)

# Function that Display the menu feature.
def menuFeature(stdID, student_level, _degree, count):
    # Prints the Menu and ask the user for the feature.
    print('\033[1m' + 'Student Transcript Generation System' + '\033[0m')
    print('==================================================')
    print('1. Student details\n2. Statistics\n3. Transcript based on major courses\n4. Transcript based on minor courses')
    print('5. Full transcript\n6. Previous transcript requests\n7. Select another student\n8. Terminate the system')
    print('==================================================')
    feature = int(input('\033[1m' + 'Enter Your Feature: ' + '\033[0m'))

    # Condtitional statement that checks for the feature that the user selecteed then run the appropriate function for that feature.
    if feature == 1:
        detailsFeature(stdID, student_level, _degree, count)
    elif feature == 2:
        statisticsFeature(stdID, student_level, _degree, count)
    elif feature == 3:
        majorTranscriptFeature(stdID, student_level, _degree, count)
    elif feature == 4:
        minorTranscriptFeature(stdID, student_level, _degree, count)
    elif feature == 5:
        fullTranscriptFeature(stdID, student_level, _degree, count)
    elif feature == 6:
        previousRequestsFeature(stdID, student_level, _degree, count)
    elif feature == 7:
        newStudentFeature()
    elif feature == 8:
        terminateFeature(count)

# Function that show the details of the student
def detailsFeature(stdID, student_level, _degree, count):
    count += 1
    File = open(f"std{stdID}PreviousRequest.txt", 'a+')
    File.write(f"Student Details \t\t{DateToday:>10} \t\t{TimeNow:>10}\n")
    File.read()
    # Open the studentDetails.csv
    with open('studentDetails.csv') as studentDetails:
        sdtDetails = csv.reader(studentDetails)
        for row in sdtDetails:
            # Checks the student ID in each row.
            if stdID in row:
                # Checks if the degree is undergraduate and print the appropriate details.
                if 'U' in row:
                    name = row[2]
                    std_id = row[1]
                    level = row[5]
                    degree = row[6]
                    n_terms = row[9]
                    college = row[3]
                    dept = row[4]
                    format = (f"Name: {name}\nStudent ID: {std_id}\nLevel(s): {level}\nDegree: {degree}\nNumber of Terms: {n_terms}\nCollege(s): {college}\nDepartment(s): {dept}")
                    print(format)

                    filename = 'std' + stdID + 'details.txt'
                    myFile = open(filename, 'w')
                    filetext = format

                    myFile.write(filetext)
                    os.startfile(filename)
                    myFile.close()

                    time.sleep(5)
                    os.system('cls')
                    menuFeature(stdID, student_level, _degree, count)

                # Checks if the degree is Master and print the appropriate details.
                elif _degree == 'M':
                    if 'M1' in row:
                        name = row[2]
                        std_id = row[1]
                        level = row[5]
                        degree = row[6]
                        n_terms = row[9]
                        college = row[3]
                        dept = row[4]
                        format = (f"Name: {name}\nStudent ID: {std_id}\nLevel(s): {level}\nDegree: {degree}\nNumber of Terms: {n_terms}\nCollege(s): {college}\nDepartment(s): {dept}")
                        print(format)

                        filename = 'std' + stdID + 'details.txt'
                        myFile = open(filename, 'w')
                        filetext = format

                        myFile.write(filetext)
                        os.startfile(filename)
                        myFile.close()

                        time.sleep(5)
                        os.system('cls')
                        menuFeature(stdID, student_level, _degree, count)
                
                # Checks if the degree is Doctorate and print the appropriate details.
                elif _degree == 'D':
                    if 'D1' in row:
                        name = row[2]
                        std_id = row[1]
                        level = row[5]
                        degree = row[6]
                        n_terms = row[9]
                        college = row[3]
                        dept = row[4]
                        format = (f"Name: {name}\nStudent ID: {std_id}\nLevel(s): {level}\nDegree: {degree}\nNumber of Terms: {n_terms}\nCollege(s): {college}\nDepartment(s): {dept}")
                        print(format)

                        filename = 'std' + stdID + 'details.txt'
                        myFile = open(filename, 'w')
                        filetext = format

                        myFile.write(filetext)
                        os.startfile(filename)
                        myFile.close()

                        time.sleep(5)
                        os.system('cls')
                        menuFeature(stdID, student_level, _degree, count)

# Functions that display the statistic of the student.
def statisticsFeature(stdID, student_level, _degree, count):
    count += 1
    File = open(f"std{stdID}PreviousRequest.txt", 'a+')
    File.write(f"Student Statistics \t\t{DateToday:>10} \t\t{TimeNow:>10}\n")
    File.read()
    # Open the student statistics.
    with open(f"{stdID}.csv") as statistics:
        stdStats = csv.reader(statistics)
        heading = next(stdStats)
        # For Undergraduate
        if student_level == 'U':
            terms = []
            term1 = []
            term2 = []
            term3 = []
            term4 = []
            term5 = []

            all_grades = []
            # For loop that will store the grades of the student.
            for row in stdStats:
                terms.append(int(row[2]))
                if 'U' in row:
                    all_grades.append(int(row[7]))
                    if '1' in row[2]:
                        term1.append(int(row[7]))
                    elif '2' in row[2]:
                        term2.append(int(row[7]))
                    elif '3' in row[2]:
                        term3.append(int(row[7]))
                    elif '4' in row[2]:
                        term4.append(int(row[7]))
                    elif '5' in row[2]:
                        term5.append(int(row[7]))

            # Get the overall average as well as the average in each term.
            ave_grades = st.mean(all_grades)
            ave_term1 = st.mean(term1)
            ave_term2 = st.mean(term2)
            ave_term3 = st.mean(term3)
            ave_term4 = st.mean(term4)
            ave_term5 = st.mean(term5)

            # Check the maximum grade and in what term.
            max_grades = int(max(all_grades))
            for gt in range(len(all_grades)):
                grade_ = int(all_grades[gt])
                if grade_ == max_grades:
                    max_grades_term = terms[gt]
                    break
            
            # Check the minimum grade and in what term.
            min_grades = int(min(all_grades))
            for gt in range(len(all_grades)):
                grade_ = int(all_grades[gt])
                if grade_ == min_grades:
                    min_grades_term = terms[gt]
                    break
            
            # Print the Statistic data in the console.
            print(f"""============================================================
*****************\t Undergraduate Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_grades:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1:.2f}
\t Term 2: {ave_term2:.2f}
\t Term 3: {ave_term3:.2f}
\t Term 4: {ave_term4:.2f}
\t Term 5: {ave_term5:.2f}
Maximum grade(s) and in which terms(s): {max_grades:.2f} in Term: {max_grades_term}
Minimum grade(s) and in which term(s): {min_grades:.2f} in Term: {min_grades_term}
Do you have any repeated course(s)? None""")
            
            # Create a txt file containing the student ID
            filename = "std" + stdID + "statistics.txt"
            myFile = open(filename, 'w')
            # Stores the data
            myFile.write(f"""============================================================
****************\t Undergraduate Level\t ****************
============================================================
Overall average (major and minor) for all terms: {ave_grades:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1:.2f}
\t Term 2: {ave_term2:.2f}
\t Term 3: {ave_term3:.2f}
\t Term 4: {ave_term4:.2f}
\t Term 5: {ave_term5:.2f}
Maximum grade(s) and in which terms(s): {max_grades:.2f} in Term: {max_grades_term}
Minimum grade(s) and in which term(s): {min_grades:.2f} in Term: {min_grades_term}
Do you have any repeated course(s)? None""")
            # Open the txt file
            os.startfile(filename)
            myFile.close()
            
            time.sleep(5)
            os.system('cls')
            menuFeature(stdID, student_level, _degree, count)
        
        # For Graduate
        elif student_level == 'G':
            # Master
            if _degree == 'M':
                terms = []
                term1 = []
                term2 = []
                term3 = []
                all_grades = []
                # For loop that will store the grades of the student.
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'M1' in row[1]:
                        all_grades.append(int(row[7]))
                        if '1' in row[2]:
                            term1.append(int(row[7]))
                        elif '2' in row[2]:
                            term2.append(int(row[7]))
                        elif '3' in row[2]:
                            term3.append(int(row[7]))
                
                # Get the overall average as well as the average in each term.
                ave_grades = st.mean(all_grades)
                ave_term1 = st.mean(term1)
                ave_term2 = st.mean(term2)
                ave_term3 = st.mean(term3)

                # Check the maximum grade and in what term.
                max_grades = int(max(all_grades))
                for gt in range(len(all_grades)):
                    grade_ = int(all_grades[gt])
                    if grade_ == max_grades:
                        max_grades_term = terms[gt]
                        break
                
                # Check the minimum grade and in what term.
                min_grades = int(min(all_grades))
                for gt in range(len(all_grades)):
                    grade_ = int(all_grades[gt])
                    if grade_ == min_grades:
                        min_grades_term = terms[gt]
                        break
                
                # Print the Statistic data in the console.
                print(f"""
============================================================
******************** Graduate(M) Level *********************
============================================================
Overall average (major and minor) for all terms: {ave_grades:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1:.2f}
\t Term 2: {ave_term2:.2f}
\t Term 3: {ave_term3:.2f}
Maximum grade(s) and in which terms(s): {max_grades:.2f} in Term: {max_grades_term}
Minimum grade(s) and in which term(s): {min_grades:.2f} in Term: {min_grades_term}
Do you have any repeated course(s)? None""")
               
               # Create a txt file
                filename = "std" + stdID + "statistics.txt"
                myFile = open(filename, 'w')
                # Stores the Data in the txt file
                myFile.write(f"""============================================================
*****************\t Graduate(M) Level\t *****************
============================================================
Overall average (major and minor) for all terms: {ave_grades:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1:.2f}
\t Term 2: {ave_term2:.2f}
\t Term 3: {ave_term3:.2f}
Maximum grade(s) and in which terms(s): {max_grades:.2f} in Term: {max_grades_term}
Minimum grade(s) and in which term(s): {min_grades:.2f} in Term: {min_grades_term}
Do you have any repeated course(s)? None""")
                # Open the txt file.
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)

            # For Doctorate
            elif _degree == 'D':
                terms = []
                term1 = []
                term2 = []
                term3 = []
                term4 = []
                all_grades = []
                # For loop that get the grade of the graduate student.
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'D1' in row[1]:
                        all_grades.append(int(row[7]))
                        if '1' in row[2]:
                            term1.append(int(row[7]))
                        elif '2' in row[2]:
                            term2.append(int(row[7]))
                        elif '3' in row[2]:
                            term3.append(int(row[7]))
                        elif '4' in row[2]:
                            term4.append(int(row[7]))
                
                # Get the overall average as well as the average in each term.
                ave_grades = st.mean(all_grades)
                ave_term1 = st.mean(term1)
                ave_term2 = st.mean(term2)
                ave_term3 = st.mean(term3)
                ave_term4 = st.mean(term4)

                # Check the maximum grade and in what term.
                max_grades = int(max(all_grades))
                for gt in range(len(all_grades)):
                    grade_ = int(all_grades[gt])
                    if grade_ == max_grades:
                        max_grades_term = terms[gt]
                        break
                
                # Check the minimum grade and in what term.
                min_grades = int(min(all_grades))
                for gt in range(len(all_grades)):
                    grade_ = int(all_grades[gt])
                    if grade_ == min_grades:
                        min_grades_term = terms[gt]
                        break
                
                # Print the statistic Data.
                print(f"""
============================================================
******************\t Graduate(D) Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_grades:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1:.2f}
\t Term 2: {ave_term2:.2f}
\t Term 3: {ave_term3:.2f}
\t Term 4: {ave_term4:.2f}
Maximum grade(s) and in which terms(s): {max_grades:.2f} in Term: {max_grades_term}
Minimum grade(s) and in which term(s): {min_grades:.2f} in Term: {min_grades_term}
Do you have any repeated course(s)? None""")

                filename = "std" + stdID + "statistics.txt"
                myFile = open(filename, 'w')
                myFile.write(f"""============================================================
*****************\t Graduate(D) Level\t *****************
============================================================
Overall average (major and minor) for all terms: {ave_grades:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1:.2f}
\t Term 2: {ave_term2:.2f}
\t Term 3: {ave_term3:.2f}
\t Term 4: {ave_term4:.2f}
Maximum grade(s) and in which terms(s): {max_grades:.2f} in Term: {max_grades_term}
Minimum grade(s) and in which term(s): {min_grades:.2f} in Term: {min_grades_term}
Do you have any repeated course(s)? None""")
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)

                # For Both
            elif _degree == 'B0':
                terms = []
                term1 = []
                term2 = []
                term3 = []
                term4 = []
                all_grades = []
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'M1' or 'D1' in row[1]:
                        all_grades.append(int(row[7]))
                        if '1' in row[2]:
                            term1.append(int(row[7]))
                        elif '2' in row[2]:
                            term2.append(int(row[7]))
                        elif '3' in row[2]:
                            term3.append(int(row[7]))
                        elif '4' in row[2]:
                            term4.append(int(row[7]))
                
                ave_grades = st.mean(all_grades)
                ave_term1 = st.mean(term1)
                ave_term2 = st.mean(term2)
                ave_term3 = st.mean(term3)
                ave_term4 = st.mean(term4)

                max_grades = int(max(all_grades))
                for gt in range(len(all_grades)):
                    grade_ = int(all_grades[gt])
                    if grade_ == max_grades:
                        max_grades_term = terms[gt]
                        break
                
                min_grades = int(min(all_grades))
                for gt in range(len(all_grades)):
                    grade_ = int(all_grades[gt])
                    if grade_ == min_grades:
                        min_grades_term = terms[gt]
                        break

                print(f"""
============================================================
***************\t Graduate(M and D) Level\t ***************
============================================================
Overall average (major and minor) for all terms: {ave_grades}
Average (major and minor) of each term:
\t Term 1: {ave_term1}
\t Term 2: {ave_term2}
\t Term 3: {ave_term3}
\t Term 4: {ave_term4}
Maximum grade(s) and in which terms(s): {max_grades} in Term: {max_grades_term}
Minimum grade(s) and in which term(s): {min_grades} in Term: {min_grades_term}
Do you have any repeated course(s)? None""")

                filename = "std" + stdID + "statistics.txt"
                myFile = open(filename, 'w')
                myFile.write(f"""============================================================
**************\t Graduate(M and D) Level\t **************
============================================================
Overall average (major and minor) for all terms: {ave_grades}
Average (major and minor) of each term:
\t Term 1: {ave_term1}
\t Term 2: {ave_term2}
\t Term 3: {ave_term3}
\t Term 4: {ave_term4}
Maximum grade(s) and in which terms(s): {max_grades} in Term: {max_grades_term}
Minimum grade(s) and in which term(s): {min_grades} in Term: {min_grades_term}
Do you have any repeated course(s)? None""")
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)
        
# Function for Major Transcript
def majorTranscriptFeature(stdID, student_level, _degree, count):
    count += 1
    File = open(f"std{stdID}PreviousRequest.txt", 'a+')
    File.write(f"Major Transcript \t\t{DateToday:>10} \t\t{TimeNow:>10}\n")
    File.read()
    # Open the student detaild.csv
    sdtD = open('studentDetails.csv')
    sdtDetails = csv.reader(sdtD)
    heading = next(sdtDetails)
    #For Loop that get the details of the student
    for row in sdtDetails:
        if stdID in row:
            name = row[2]
            std_id = row[1]
            level = row[5]
            n_terms = row[9]
            college = row[3]
            dept = row[4]
            major = row[7]
            minor = row[8]
            break
    # Create a txt file with the student ID
    filename = "std" + stdID + "MajorTranscript.txt"
    myFile = open(filename, 'w')

    # Print and store the data in the txt
    print(f'Name: {name} \t\tstdID: {std_id}\nCollege(s):{college}\t\tDepartment(s): {dept}\nMajor: {major} \t\tMinor: {minor}\nLevel:  {level} \t\t\tNumber of Terms: {n_terms}\n')
    myFile.write(f'Name: {name} \t\tstdID: {std_id}\nCollege(s):{college}\t\tDepartment(s): {dept}\nMajor: {major} \t\tMinor: {minor}\nLevel:  {level} \t\t\tNumber of Terms: {n_terms}\n')
    
    #Open the student statistics.
    with open(f"{stdID}.csv") as statistics:
        stdStats = csv.reader(statistics)
        heading = next(stdStats)
        # For Undergraduate
        if student_level == 'U':
            terms = []
            term1 = []
            term2 = []
            term3 = []
            term4 = []
            term5 = []

            all_grades = []
            # For loop that get the grades of the student
            for row in stdStats:
                terms.append(int(row[2]))
                if 'U' in row:
                    if 'Major' in row:
                        all_grades.append(int(row[7]))
                        if '1' in row[2]:
                            term1.append(int(row[7]))
                        elif '2' in row[2]:
                            term2.append(int(row[7]))
                        elif '3' in row[2]:
                            term3.append(int(row[7]))
                        elif '4' in row[2]:
                            term4.append(int(row[7]))
                        elif '5' in row[2]:
                            term5.append(int(row[7]))

            # Get the overall average and the average each term
            ave_grades = st.mean(all_grades)
            ave_term1 = st.mean(term1)
            ave_term2 = st.mean(term2)
            ave_term3 = st.mean(term3)
            ave_term4 = st.mean(term4)
            ave_term5 = st.mean(term5)

            # Print the data in the console and store it in the txt file
            print("""
============================================================
*************  Major Transcript for Level (U)  *************
============================================================\n""")
            myFile.write("""
============================================================
*************  Major Transcript for Level (U)  *************
============================================================\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 1) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term1:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term1:.2f}       Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term2:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term2:.2f}       Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term3:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term3:.2f}       Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term4:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term4:.2f}       Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term5:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_term5:.2f}       Overall Average: {ave_grades:.2f}\n""")
            print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
            myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
            os.startfile(filename)
            myFile.close()

            time.sleep(5)
            os.system('cls')
            menuFeature(stdID, student_level, _degree, count)

        # Graduate
        elif student_level == 'G':
            # Checks the degree if masteral
            if _degree == 'M':
                terms = []
                term1 = []
                term2 = []
                term3 = []

                all_grades = []
                # For loop that get the grades
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'G' in row:
                        if 'M1' in row:
                            if 'Major' in row:
                                all_grades.append(int(row[7]))
                                if '1' in row[2]:
                                    term1.append(int(row[7]))
                                elif '2' in row[2]:
                                    term2.append(int(row[7]))
                                elif '3' in row[2]:
                                    term3.append(int(row[7]))

                # Get the avarage in all grades
                ave_grades = st.mean(all_grades)

                #Print and store the data in the txt as well as in the console
                print("""
============================================================
************  Major Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
************  Major Transcript for Level (G-M)  ************
============================================================\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term1):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term1):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term2):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term2):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term3):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term3):.2f}       Overall Average: {ave_grades:.2f}\n""")
                print("""
============================================================
***********  End of Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
***********  End of Transcript for Level (G-M)  ************
============================================================\n""")
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)

            # Doctorate
            elif _degree == 'D':
                terms = []
                term1 = []
                term2 = []
                term3 = []
                term4 = []

                all_grades = []
                # For loop get the grades of the student
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'D1' in row:
                        if 'Major' in row:
                            all_grades.append(int(row[7]))
                            if '1' in row[2]:
                                term1.append(int(row[7]))
                            elif '2' in row[2]:
                                term2.append(int(row[7]))
                            elif '3' in row[2]:
                                term3.append(int(row[7]))
                            elif '4' in row[2]:
                                term4.append(int(row[7]))

                # Get the average of the student
                ave_grades = st.mean(all_grades)

                #Print and store data in txt file as well as in the console
                print("""
============================================================
*************  Major Transcript for Level (G-D)  ***********
============================================================\n""")
                myFile.write("""
============================================================
*************  Major Transcript for Level (G-D)  ***********
============================================================\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term1)}       Overall Average: {ave_grades}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term1)}       Overall Average: {ave_grades}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term2):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term2):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term3):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term3):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term4):.2f}       Overall Average: {ave_grades:.2f}""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {st.mean(term4):.2f}       Overall Average: {ave_grades:.2f}""")
                
                print("""
============================================================
*************  End of Transcript for Level (G-D)  **********
============================================================\n""")
                myFile.write("""
============================================================
*************  End of Transcript for Level (G-D)  **********
============================================================\n""")
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)

# Function for the minor Transcript of the student/graduate
def minorTranscriptFeature(stdID, student_level, _degree, count):
    count += 1
    File = open(f"std{stdID}PreviousRequest.txt", 'a+')
    File.write(f"Minor Transcript \t\t{DateToday:>10} \t\t{TimeNow:>10}\n")
    File.read()
    #Open the student details.
    sdtD = open('studentDetails.csv')
    sdtDetails = csv.reader(sdtD)
    heading = next(sdtDetails)
    #For loop that get the information of the student/graduate
    for row in sdtDetails:
        if stdID in row:
            name = row[2]
            std_id = row[1]
            level = row[5]
            n_terms = row[9]
            college = row[3]
            dept = row[4]
            major = row[7]
            minor = row[8]
            break
    
    #Create a txt file with the student ID
    filename = "std" + stdID + "MinorTranscript.txt"
    myFile = open(filename, 'w')
    
    #Print and store the data in the txt,
    print(f'Name: {name} \t\tstdID: {std_id}\nCollege(s):{college}\t\tDepartment(s): {dept}\nMajor: {major} \t\tMinor: {minor}\nLevel:  {level} \t\t\tNumber of Terms: {n_terms}\n')
    myFile.write(f'Name: {name} \t\tstdID: {std_id}\nCollege(s):{college}\t\tDepartment(s): {dept}\nMajor: {major} \t\tMinor: {minor}\nLevel:  {level} \t\t\tNumber of Terms: {n_terms}\n')
    
    # Open the student statistics
    with open(f"{stdID}.csv") as statistics:
        stdStats = csv.reader(statistics)
        heading = next(stdStats)
        # For Undergraduate
        if student_level == 'U':
            terms = []
            term1 = []
            term2 = []
            term3 = []
            term4 = []
            term5 = []

            all_grades = []
            # For loop that get the grades
            for row in stdStats:
                terms.append(int(row[2]))
                if 'U' in row:
                    if 'Minor' in row:
                        all_grades.append(int(row[7]))
                        if '1' in row[2]:
                            term1.append(int(row[7]))
                        elif '2' in row[2]:
                            term2.append(int(row[7]))
                        elif '3' in row[2]:
                            term3.append(int(row[7]))
                        elif '4' in row[2]:
                            term4.append(int(row[7]))
                        elif '5' in row[2]:
                            term5.append(int(row[7]))

            # Get the average grade
            ave_grades = st.mean(all_grades)
            ave_term1 = st.mean(term1)
            ave_term2 = st.mean(term2)
            ave_term3 = st.mean(term3)
            ave_term4 = st.mean(term4)
            ave_term5 = st.mean(term5)

            #Print and stores the data in the txt file
            print("""
============================================================
*************  Minor Transcript for Level (U)  *************
============================================================\n""")
            myFile.write("""
============================================================
*************  Minor Transcript for Level (U)  *************
============================================================\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 1) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term1:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term1:.2f}       Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term2:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term2:.2f}       Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term3:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term3:.2f}       Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term4:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term4:.2f}       Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term5:.2f}       Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term5:.2f}       Overall Average: {ave_grades:.2f}\n""")
            print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
            myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
            os.startfile(filename)
            myFile.close()

            time.sleep(5)
            os.system('cls')
            menuFeature(stdID, student_level, _degree, count)
        
        # Graduate
        elif student_level == 'G':
            # Master
            if _degree == 'M':
                terms = []
                term1 = []
                term2 = []
                term3 = []

                all_grades = []
                #For loop that get the grades of the student
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'G' in row:
                        if 'M1' in row:
                            if 'Minor' in row:
                                all_grades.append(int(row[7]))
                                if '1' in row[2]:
                                    term1.append(int(row[7]))
                                elif '2' in row[2]:
                                    term2.append(int(row[7]))
                                elif '3' in row[2]:
                                    term3.append(int(row[7]))

                # Get the average grade of the student
                ave_grades = st.mean(all_grades)

                #Print and Store the data in the txt file
                print("""
============================================================
************  Minor Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
************  Minor Transcript for Level (G-M)  ************
============================================================\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3):.2f}       Overall Average: {ave_grades:.2f}\n""")
                print("""
============================================================
***********  End of Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
***********  End of Transcript for Level (G-M)  ************
============================================================\n""")
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)

            # Doctoral
            elif _degree == 'D':
                terms = []
                term1 = []
                term2 = []
                term3 = []
                term4 = []

                all_grades = []
                #For Loop that get the grades of the student
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'D1' in row:
                        if 'Minor' in row:
                            all_grades.append(int(row[7]))
                            if '1' in row[2]:
                                term1.append(int(row[7]))
                            elif '2' in row[2]:
                                term2.append(int(row[7]))
                            elif '3' in row[2]:
                                term3.append(int(row[7]))
                            elif '4' in row[2]:
                                term4.append(int(row[7]))

                # Get the average of the student
                ave_grades = st.mean(all_grades)

                # Print and stores the data in the txt file
                print("""
============================================================
*************  Minor Transcript for Level (G-D)  ***********
============================================================\n""")
                myFile.write("""
============================================================
*************  Minor Transcript for Level (G-D)  ***********
============================================================\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3):.2f}       Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3):.2f}       Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term4):.2f}       Overall Average: {ave_grades:.2f}""")
                myFile.write(f"""============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term4):.2f}       Overall Average: {ave_grades:.2f}""")
                print("""
============================================================
*************  End of Transcript for Level (G-D)  **********
============================================================\n""")
                myFile.write("""
============================================================
*************  End of Transcript for Level (G-D)  **********
============================================================\n""")
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)

# Function that shows the full transcript of the student/graduate
def fullTranscriptFeature(stdID, student_level, _degree, count):
    count += 1
    File = open(f"std{stdID}PreviousRequest.txt", "a+")
    File.write(f"Full Transcripts \t\t{DateToday:>10} \t\t{TimeNow:>10}\n")
    File.read()
    # Open the student details.
    sdtD = open('studentDetails.csv')
    sdtDetails = csv.reader(sdtD)
    heading = next(sdtDetails)
    # For loop that get the student information
    for row in sdtDetails:
        if stdID in row:
            name = row[2]
            std_id = row[1]
            level = row[5]
            n_terms = row[9]
            college = row[3]
            dept = row[4]
            major = row[7]
            minor = row[8]
            break
    
    # Create a txt filw with the student number
    filename = "std" + stdID + "FullTranscript.txt"
    myFile = open(filename, 'w')

    # Print and stores the data in the txt file 
    print(f'Name: {name} \t\tstdID: {std_id}\nCollege(s):{college}\t\tDepartment(s): {dept}\nMajor: {major} \t\tMinor: {minor}\nLevel:  {level} \t\t\tNumber of Terms: {n_terms}\n')
    myFile.write(f'Name: {name} \t\tstdID: {std_id}\nCollege(s):{college}\t\tDepartment(s): {dept}\nMajor: {major} \t\tMinor: {minor}\nLevel:  {level} \t\t\tNumber of Terms: {n_terms}\n')

    # Open the student statistics
    with open(f"{stdID}.csv") as statistics:
        stdStats = csv.reader(statistics)
        heading = next(stdStats)
        # For Undergraduate
        if student_level == 'U':
            terms = []
            Majterm1 = []
            Majterm2 = []
            Majterm3 = []
            Majterm4 = []
            Majterm5 = []
            Minterm1 = []
            Minterm2 = []
            Minterm3 = []
            Minterm4 = []
            Minterm5 = []

            all_grades = []
            #For loop that get the grades of the student
            for row in stdStats:
                terms.append(int(row[2]))
                if 'U' in row:
                    if 'Major' in row:
                        all_grades.append(int(row[7]))
                        if '1' in row[2]:
                            Majterm1.append(int(row[7]))
                        elif '2' in row[2]:
                            Majterm2.append(int(row[7]))
                        elif '3' in row[2]:
                            Majterm3.append(int(row[7]))
                        elif '4' in row[2]:
                            Majterm4.append(int(row[7]))
                        elif '5' in row[2]:
                            Majterm5.append(int(row[7]))
                    else:
                        all_grades.append(int(row[7]))
                        if '1' in row[2]:
                            Minterm1.append(int(row[7]))
                        elif '2' in row[2]:
                            Minterm2.append(int(row[7]))
                        elif '3' in row[2]:
                            Minterm3.append(int(row[7]))
                        elif '4' in row[2]:
                            Minterm4.append(int(row[7]))
                        elif '5' in row[2]:
                            Minterm5.append(int(row[7]))

            # Get the overall average as well as the average in each term
            ave_grades = st.mean(all_grades)
            ave_Majterm1 = st.mean(Majterm1)
            ave_Majterm2 = st.mean(Majterm2)
            ave_Majterm3 = st.mean(Majterm3)
            ave_Majterm4 = st.mean(Majterm4)
            ave_Majterm5 = st.mean(Majterm5)
            ave_Minterm1 = st.mean(Minterm1)
            ave_Minterm2 = st.mean(Minterm2)
            ave_Minterm3 = st.mean(Minterm3)
            ave_Minterm4 = st.mean(Minterm4)
            ave_Minterm5 = st.mean(Minterm5)

            # Print and store the grades in the txt file
            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 1) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
            print(f"""
============================================================
***********************  Term 1  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1:.2f}       Minor Average: {ave_Minterm1:.2f} 
Term Average: {st.mean(Majterm1 + Minterm1):.2f}        Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
***********************  Term 1  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1:.2f}       Minor Average: {ave_Minterm1:.2f} 
Term Average: {st.mean(Majterm1 + Minterm1):.2f}        Overall Average: {ave_grades:.2f}\n""")
            
            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
            print(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2:.2f}       Minor Average: {ave_Minterm2:.2f}   
Term Average: {st.mean(Majterm2 + Minterm2):.2f}        Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2:.2f}       Minor Average: {ave_Minterm2:.2f}   
Term Average: {st.mean(Majterm2 + Minterm2):.2f}        Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
            print(f"""
============================================================
***********************  Term 3  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3:.2f}       Minor Average: {ave_Minterm3:.2f}  
Term Average: {st.mean(Majterm3 + Minterm3):.2f}        Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3:.2f}       Minor Average: {ave_Minterm3:.2f}  
Term Average: {st.mean(Majterm3 + Minterm3):.2f}        Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4:.2f}       Minor Average: {ave_Minterm4:.2f}  
Term Average: {st.mean(Majterm4 + Minterm4):.2f}        Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4:.2f}       Minor Average: {ave_Minterm4:.2f}  
Term Average: {st.mean(Majterm4 + Minterm4):.2f}        Overall Average: {ave_grades:.2f}\n""")

            df = pd.read_csv(f"{stdID}.csv")
            df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
            print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm5:.2f}       Minor Average: {ave_Minterm5:.2f}  
Term Average: {st.mean(Majterm5 + Minterm5):.2f}        Overall Average: {ave_grades:.2f}\n""")
            myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm5:.2f}       Minor Average: {ave_Minterm5:.2f}  
Term Average: {st.mean(Majterm5 + Minterm5):.2f}        Overall Average: {ave_grades:.2f}\n""")
            print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================""")
            myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================""")
            os.startfile(filename)
            myFile.close()

            time.sleep(5)
            os.system('cls')
            menuFeature(stdID, student_level, _degree, count)
        
        # Full Transcripts for Graduates
        elif student_level == 'G':
            # Masters
            if _degree == 'M':
                terms = []
                Majterm1 = []
                Majterm2 = []
                Majterm3 = []
                Minterm1 = []
                Minterm2 = []
                Minterm3 = []
                all_grades = []
                #For loop that get the grade of the student
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'M1' in row:
                        if 'Major' in row:
                            all_grades.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3.append(int(row[7]))
                        else:
                            all_grades.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3.append(int(row[7]))

                # Get the overall average and the average each term
                ave_grades = st.mean(all_grades)
                ave_Majterm1 = st.mean(Majterm1)
                ave_Majterm2 = st.mean(Majterm2)
                ave_Majterm3 = st.mean(Majterm3)
                ave_Minterm1 = st.mean(Minterm1)
                ave_Minterm2 = st.mean(Minterm2)
                ave_Minterm3 = st.mean(Minterm3)

                # Print and store the data in the txt file
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1:.2f}       Minor Average: {ave_Minterm1:.2f} 
Term Average: {st.mean(Majterm1 + Minterm1):.2f}            Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1:.2f}       Minor Average: {ave_Minterm1:.2f} 
Term Average: {st.mean(Majterm1 + Minterm1):.2f}            Overall Average: {ave_grades:.2f}\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2:.2f}       Minor Average: {ave_Minterm2:.2f}   
Term Average: {st.mean(Majterm2 + Minterm2):.2f}            Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2:.2f}       Minor Average: {ave_Minterm2:.2f}   
Term Average: {st.mean(Majterm2 + Minterm2):.2f}            Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3:.2f}       Minor Average: {ave_Minterm3:.2f}  
Term Average: {st.mean(Majterm3 + Minterm3):.2f}            Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3:.2f}       Minor Average: {ave_Minterm3:.2f}  
Term Average: {st.mean(Majterm3 + Minterm3):.2f}            Overall Average: {ave_grades:.2f}\n""")
                print("""
============================================================
************  End of Transcript for Level (G-M)  ***********
============================================================\n""")
                myFile.write("""
============================================================
************  End of Transcript for Level (G-M)  ***********
============================================================\n""")
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)
            
            # Full Transcript of Doctoral Graduate
            elif _degree == 'D':
                terms = []
                Majterm1 = []
                Majterm2 = []
                Majterm3 = []
                Majterm4 = []
                Minterm1 = []
                Minterm2 = []
                Minterm3 = []
                Minterm4 = []
                all_grades = []
                # FOr loop that get the student grades
                for row in stdStats:
                    terms.append(int(row[2]))
                    if 'D1' in row:
                        if 'Major' in row:
                            all_grades.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3.append(int(row[7]))
                            elif '4' in row[2]:
                                Majterm4.append(int(row[7]))
                        else:
                            all_grades.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3.append(int(row[7]))
                            elif '4' in row[2]:
                                Minterm4.append(int(row[7]))

                #Get the overall average and average each term.
                ave_grades = st.mean(all_grades)
                ave_Majterm1 = st.mean(Majterm1)
                ave_Majterm2 = st.mean(Majterm2)
                ave_Majterm3 = st.mean(Majterm3)
                ave_Majterm4 = st.mean(Majterm4)
                ave_Minterm1 = st.mean(Minterm1)
                ave_Minterm2 = st.mean(Minterm2)
                ave_Minterm3 = st.mean(Minterm3)
                ave_Minterm4 = st.mean(Minterm4)

                #Print and stores the data in the txt file
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1:.2f}       Minor Average: {ave_Minterm1:.2f} 
Term Average: {st.mean(Majterm1 + Minterm1):.2f}            Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1:.2f}       Minor Average: {ave_Minterm1:.2f} 
Term Average: {st.mean(Majterm1 + Minterm1):.2f}            Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2:.2f}       Minor Average: {ave_Minterm2:.2f}   
Term Average: {st.mean(Majterm2 + Minterm2):.2f}            Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2:.2f}       Minor Average: {ave_Minterm2:.2f}   
Term Average: {st.mean(Majterm2 + Minterm2):.2f}            Overall Average: {ave_grades:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3:.2f}       Minor Average: {ave_Minterm3:.2f}  
Term Average: {st.mean(Majterm3 + Minterm3):.2f}            Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3:.2f}       Minor Average: {ave_Minterm3:.2f}  
Term Average: {st.mean(Majterm3 + Minterm3):.2f}            Overall Average: {ave_grades:.2f}\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4:.2f}       Minor Average: {ave_Minterm4:.2f}  
Term Average: {st.mean(Majterm4 + Minterm4):.2f}            Overall Average: {ave_grades:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4:.2f}       Minor Average: {ave_Minterm4:.2f}  
Term Average: {st.mean(Majterm4 + Minterm4):.2f}            Overall Average: {ave_grades:.2f}\n""")
                print("""
============================================================
************  End of Transcript for Level (G-D)  ***********
============================================================\n""")
                myFile.write("""
============================================================
************  End of Transcript for Level (G-D)  ***********
============================================================\n""")
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)

# Function that shows the previous requests of the user.
def previousRequestsFeature(stdID, student_level, _degree, count):
    File = open(f"std{stdID}PreviousRequest.txt", 'a+')
    File.write("==================================================================\n")
    File.write(f"\tRequest\t\t\t   Date\t\t\t   Time \n")
    File.write("==================================================================\n")
    File.read()

    File = open(f"std{stdID}PreviousRequest.txt", 'r')
    Show = File.read()
    os.startfile(f"std{stdID}PreviousRequest.txt")
    print(Show)
    File.close()

    time.sleep(4)
    os.system("cls")
    menuFeature(stdID, student_level, _degree, count)

# Function that restart the program and ask the use for new student
def newStudentFeature():
    os.system('cls')
    startFeature()

# Terminate the program and show the requests of the user.
def terminateFeature(count):
    print(f"The number of requests made is {count}")
    print("Thank you for using the Student Transcript Generation System!")
    exit()

# Calls the function startfeature.
startFeature()