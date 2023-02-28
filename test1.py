# MAJOR
import csv
import pandas as pd
import numpy as np
import statistics as st

stdID = '201101000'
student_level = 'G'
_degree = 'D1'

def MajorTranscriptFeatureUndergraduate():
    with open('StudentDetails.csv') as studentDetails:
        read = csv.reader(studentDetails)
        heading = next(studentDetails)
        for row in read:
            if student_level == 'U':
                if stdID in row:
                    if student_level in row:
                        name = row[2]
                        std_id = row[1]
                        level = row[5]
                        degree = row[6]
                        n_terms = row[9]
                        college = row[3]
                        dept = row[4]
                        major = row[7]
                        minor = row[8]
                        format = (f"""Name: {name} \t Student ID: {std_id}
    College(s): {college} \t\t Department(s): {dept}
    Major: {major} \t\t Minor: {minor}
    Level(s): {level} \t\t\t Degree: {degree}
    Number of Terms: {n_terms}""")
                        print("""
    ============================================================
    *************  Major Transcript for Level (U)  *************
    ============================================================""")
                        print(format)
                        with open(f"{stdID}.csv") as statistics:
                            stdStats = csv.reader(statistics)
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

                                    ave_grades = str(st.mean(all_grades))

                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 1) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 1  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {st.mean(term1)}       Overall Average: {ave_grades}""")
                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 2  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {st.mean(term2)}       Overall Average: {ave_grades}""")
                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 3  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {st.mean(term3)}       Overall Average: {ave_grades}""")
                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 4  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {st.mean(term4)}       Overall Average: {ave_grades}""")
                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 5  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {st.mean(term5)}       Overall Average: {ave_grades}""")
                                    print("""
    ============================================================
    *************  End of Transcript for Level (U)  ************
    ============================================================""")

def MajorTranscriptFeatureGraduateMasteral():
    with open('StudentDetails.csv') as studentDetails:
        read = csv.reader(studentDetails)
        heading = next(studentDetails)
        for row in read:
            if student_level == 'G':
                if 'M1' in row:
                    if stdID in row:
                        if student_level in row:
                            name = row[2]
                            std_id = row[1]
                            level = row[5]
                            degree = row[6]
                            n_terms = row[9]
                            college = row[3]
                            dept = row[4]
                            major = row[7]
                            minor = row[8]
                            format = (f"""Name: {name} \t Student ID: {std_id}
        College(s): {college} \t\t Department(s): {dept}
        Major: {major} \t\t Minor: {minor}
        Level(s): {level} \t\t\t Degree: {degree}
        Number of Terms: {n_terms}""")
                            print("""
    ============================================================
    ************  Major Transcript for Level (G-M)  ************
    ============================================================""")
                            print(format)
                            with open(f"{stdID}.csv") as statistics:
                                stdStats = csv.reader(statistics)
                                with open(f"{stdID}.csv") as statistics:
                                    stdStats = csv.reader(statistics)
                                    heading = next(stdStats)                
                                    if student_level == 'G':
                                        terms = []
                                        term1 = []
                                        term2 = []
                                        term3 = []

                                        all_grades = []
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

                                        ave_grades = str(st.mean(all_grades))

                                        df = pd.read_csv(f"{stdID}.csv")
                                        df = df[(df['Term'] == 1) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                        print(f"""
        ============================================================
        ************************  Term 1  **************************
        ============================================================
        {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
        Major Average: {st.mean(term1)}       Overall Average: {ave_grades}""")
                                        df = pd.read_csv(f"{stdID}.csv")
                                        df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                        print(f"""
        ============================================================
        ************************  Term 2  **************************
        ============================================================
        {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
        Major Average: {st.mean(term2)}       Overall Average: {ave_grades}""")
                                        df = pd.read_csv(f"{stdID}.csv")
                                        df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                        print(f"""
        ============================================================
        ************************  Term 3  **************************
        ============================================================
        {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
        Major Average: {st.mean(term3)}       Overall Average: {ave_grades}""")
                                        print("""
        ============================================================
        ***********  End of Transcript for Level (G-M)  ************
        ============================================================""")

def MajorTranscriptFeatureGraduateDoctoral():
    with open('StudentDetails.csv') as studentDetails:
        read = csv.reader(studentDetails)
        heading = next(studentDetails)
        for row in read:
            if student_level == 'G':
                if 'D1' in row:
                    if stdID in row:
                        if student_level in row:
                            name = row[2]
                            std_id = row[1]
                            level = row[5]
                            degree = row[6]
                            n_terms = row[9]
                            college = row[3]
                            dept = row[4]
                            major = row[7]
                            minor = row[8]
                            format = (f"""Name: {name} \t Student ID: {std_id}
        College(s): {college} \t\t Department(s): {dept}
        Major: {major} \t\t Minor: {minor}
        Level(s): {level} \t\t\t Degree: {degree}
        Number of Terms: {n_terms}""")
                            print("""
        ============================================================
        *************  Major Transcript for Level (G-D)  *************
        ============================================================""")
                            print(format)
                            with open(f"{stdID}.csv") as statistics:
                                stdStats = csv.reader(statistics)
                                with open(f"{stdID}.csv") as statistics:
                                    stdStats = csv.reader(statistics)
                                    heading = next(stdStats)
                                    # For Undergraduate
                                    if student_level == 'G':
                                        terms = []
                                        term1 = []
                                        term2 = []
                                        term3 = []
                                        term4 = []

                                        all_grades = []
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

                                        ave_grades = str(st.mean(all_grades))

                                        df = pd.read_csv(f"{stdID}.csv")
                                        df = df[(df['Term'] == 1) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                        print(f"""
        ============================================================
        ************************  Term 1  **************************
        ============================================================
        {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
        Major Average: {st.mean(term1)}       Overall Average: {ave_grades}""")
                                        df = pd.read_csv(f"{stdID}.csv")
                                        df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                        print(f"""
        ============================================================
        ************************  Term 2  **************************
        ============================================================
        {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
        Major Average: {st.mean(term2)}       Overall Average: {ave_grades}""")
                                        df = pd.read_csv(f"{stdID}.csv")
                                        df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                        print(f"""
        ============================================================
        ************************  Term 3  **************************
        ============================================================
        {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
        Major Average: {st.mean(term3)}       Overall Average: {ave_grades}""")
                                        df = pd.read_csv(f"{stdID}.csv")
                                        df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Major') == True)].set_index(['Level'])
                                        print(f"""
        ============================================================
        ************************  Term 4  **************************
        ============================================================
        {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
        Major Average: {st.mean(term4)}       Overall Average: {ave_grades}""")
                                        print("""
        ============================================================
        *************  End of Transcript for Level (G-D)  ************
        ============================================================""")

if student_level == 'U':
    MajorTranscriptFeatureUndergraduate()
elif student_level == 'G':
    if _degree == 'M1':
        MajorTranscriptFeatureGraduateMasteral()
    elif _degree == 'D1':
        MajorTranscriptFeatureGraduateDoctoral()
else:
    print("wews")                               