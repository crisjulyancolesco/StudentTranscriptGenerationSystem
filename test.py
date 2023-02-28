# FULL
import csv
import pandas as pd
import numpy as np
import statistics as st

stdID = '201006000'
student_level = 'U'
_degree = 'M1'



def FullTranscriptFeatureUndergraduate():
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
    *************  Full Transcript for Level (U)  **************
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

                                    ave_grades = str(st.mean(all_grades))
                                    ave_Majterm1 = str(st.mean(Majterm1))
                                    ave_Majterm2 = str(st.mean(Majterm2))
                                    ave_Majterm3 = str(st.mean(Majterm3))
                                    ave_Majterm4 = str(st.mean(Majterm4))
                                    ave_Majterm5 = str(st.mean(Majterm5))
                                    ave_Minterm1 = str(st.mean(Minterm1))
                                    ave_Minterm2 = str(st.mean(Minterm2))
                                    ave_Minterm3 = str(st.mean(Minterm3))
                                    ave_Minterm4 = str(st.mean(Minterm4))
                                    ave_Minterm5 = str(st.mean(Minterm5))

                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 1) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 1  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {ave_Majterm1}       Minor Average: {ave_Minterm1} 
    Term Average: {st.mean(Majterm1 + Minterm1)}  Overall Average: {ave_grades}""")
                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 2  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {ave_Majterm2}       Minor Average: {ave_Minterm2}   
    Term Average: {st.mean(Majterm2 + Minterm2)}                         Overall Average: {ave_grades}""")
                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 3  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {ave_Majterm3}       Minor Average: {ave_Minterm3}  
    Term Average: {st.mean(Majterm3 + Minterm3)}                         Overall Average: {ave_grades}""")
                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 4  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {ave_Majterm4}       Minor Average: {ave_Minterm4}  
    Term Average: {st.mean(Majterm4 + Minterm4)}                         Overall Average: {ave_grades}""")
                                    df = pd.read_csv(f"{stdID}.csv")
                                    df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                                    print(f"""
    ============================================================
    ************************  Term 5  **************************
    ============================================================
    {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
    Major Average: {ave_Majterm5}       Minor Average: {ave_Minterm5}  
    Term Average: {st.mean(Majterm5 + Minterm5)}                         Overall Average: {ave_grades}""")
                                    print("""
    ============================================================
    *************  End of Transcript for Level (U)  ************
    ============================================================""")

def FullTranscriptFeatureGraduateMasteral():
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
    ************  Full Transcript for Level (G-M)  *************
    ============================================================""")
                            print(format)
                            with open(f"{stdID}.csv") as statistics:
                                stdStats = csv.reader(statistics)
                                with open(f"{stdID}.csv") as statistics:
                                    stdStats = csv.reader(statistics)
                                    heading = next(stdStats)
                                    # For Undergraduate
                                    if student_level == 'G':
                                        if _degree == 'M1':
                                            terms = []
                                            Majterm1 = []
                                            Majterm2 = []
                                            Majterm3 = []
                                            Minterm1 = []
                                            Minterm2 = []
                                            Minterm3 = []

                                            all_grades = []
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

                                            ave_grades = str(st.mean(all_grades))
                                            ave_Majterm1 = str(st.mean(Majterm1))
                                            ave_Majterm2 = str(st.mean(Majterm2))
                                            ave_Majterm3 = str(st.mean(Majterm3))
                                            ave_Minterm1 = str(st.mean(Minterm1))
                                            ave_Minterm2 = str(st.mean(Minterm2))
                                            ave_Minterm3 = str(st.mean(Minterm3))

                                            df = pd.read_csv(f"{stdID}.csv")
                                            df = df[(df['Term'] == 1) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                                            print(f"""
            ============================================================
            ************************  Term 1  **************************
            ============================================================
            {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
            Major Average: {ave_Majterm1}       Minor Average: {ave_Minterm1} 
            Term Average: {st.mean(Majterm1 + Minterm1)}  Overall Average: {ave_grades}""")
                                            df = pd.read_csv(f"{stdID}.csv")
                                            df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                                            print(f"""
            ============================================================
            ************************  Term 2  **************************
            ============================================================
            {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
            Major Average: {ave_Majterm2}       Minor Average: {ave_Minterm2}   
            Term Average: {st.mean(Majterm2 + Minterm2)}                         Overall Average: {ave_grades}""")
                                            df = pd.read_csv(f"{stdID}.csv")
                                            df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                                            print(f"""
            ============================================================
            ************************  Term 3  **************************
            ============================================================
            {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
            Major Average: {ave_Majterm3}       Minor Average: {ave_Minterm3}  
            Term Average: {st.mean(Majterm3 + Minterm3)}                         Overall Average: {ave_grades}""")
                                            print("""
            ============================================================
            ***********  End of Transcript for Level (G-M)  ************
            ============================================================""")

def FullTranscriptFeatureGraduateDoctoral():
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
    ************  Full Transcript for Level (G-D)  *************
    ============================================================""")
                            print(format)
                            with open(f"{stdID}.csv") as statistics:
                                stdStats = csv.reader(statistics)
                                with open(f"{stdID}.csv") as statistics:
                                    stdStats = csv.reader(statistics)
                                    heading = next(stdStats)
                                    # For Undergraduate
                                    if student_level == 'G':
                                        if _degree == 'D1':
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

                                            ave_grades = str(st.mean(all_grades))
                                            ave_Majterm1 = str(st.mean(Majterm1))
                                            ave_Majterm2 = str(st.mean(Majterm2))
                                            ave_Majterm3 = str(st.mean(Majterm3))
                                            ave_Majterm4 = str(st.mean(Majterm4))
                                            ave_Minterm1 = str(st.mean(Minterm1))
                                            ave_Minterm2 = str(st.mean(Minterm2))
                                            ave_Minterm3 = str(st.mean(Minterm3))
                                            ave_Minterm4 = str(st.mean(Minterm4))

                                            df = pd.read_csv(f"{stdID}.csv")
                                            df = df[(df['Term'] == 1) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                                            print(f"""
            ============================================================
            ************************  Term 1  **************************
            ============================================================
            {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
            Major Average: {ave_Majterm1}       Minor Average: {ave_Minterm1} 
            Term Average: {st.mean(Majterm1 + Minterm1)}  Overall Average: {ave_grades}""")
                                            df = pd.read_csv(f"{stdID}.csv")
                                            df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                                            print(f"""
            ============================================================
            ************************  Term 2  **************************
            ============================================================
            {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
            Major Average: {ave_Majterm2}       Minor Average: {ave_Minterm2}   
            Term Average: {st.mean(Majterm2 + Minterm2)}                         Overall Average: {ave_grades}""")
                                            df = pd.read_csv(f"{stdID}.csv")
                                            df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                                            print(f"""
            ============================================================
            ************************  Term 3  **************************
            ============================================================
            {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
            Major Average: {ave_Majterm3}       Minor Average: {ave_Minterm3}  
            Term Average: {st.mean(Majterm3 + Minterm3)}                         Overall Average: {ave_grades}""")
                                            df = pd.read_csv(f"{stdID}.csv")
                                            df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                                            print(f"""
            ============================================================
            ************************  Term 4  **************************
            ============================================================
            {df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
            Major Average: {ave_Majterm4}       Minor Average: {ave_Minterm4}  
            Term Average: {st.mean(Majterm4 + Minterm4)}                         Overall Average: {ave_grades}""")
                                            print("""
            ============================================================
            ***********  End of Transcript for Level (G-D)  ************
            ============================================================""")

if student_level == 'U':
    FullTranscriptFeatureUndergraduate()
elif student_level == 'G':
    if _degree == 'M1':
        FullTranscriptFeatureGraduateMasteral()
    elif _degree == 'D1':
        FullTranscriptFeatureGraduateDoctoral()
else:
    print("wews")