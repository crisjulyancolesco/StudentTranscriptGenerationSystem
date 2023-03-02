# B and B0 options for Minor Transcript feature
            elif _degree == 'B0':
                termsM = []
                term1M = []
                term2M = []
                term3M = []
                all_gradesM = []
                termsD = []
                term1D = []
                term2D = []
                term3D = []
                term4D = []
                all_gradesD = []
                # For loop that get the grades
                for row in stdStats:
                    termsM.append(int(row[2]))
                    termsD.append(int(row[2]))
                    if 'G' in row:
                        if 'M1' in row:
                            if 'Minor' in row:
                                all_gradesM.append(int(row[7]))
                                if '1' in row[2]:
                                    term1M.append(int(row[7]))
                                elif '2' in row[2]:
                                    term2M.append(int(row[7]))
                                elif '3' in row[2]:
                                    term3M.append(int(row[7]))
                        if 'D1' in row:
                            if 'Minor' in row:
                                all_gradesD.append(int(row[7]))
                                if '1' in row[2]:
                                    term1D.append(int(row[7]))
                                elif '2' in row[2]:
                                    term2D.append(int(row[7]))
                                elif '3' in row[2]:
                                    term3D.append(int(row[7]))
                                elif '4' in row[2]:
                                    term4D.append(int(row[7]))

                # Get the avarage in all grades
                ave_gradesM = st.mean(all_gradesM)
                ave_gradesD = st.mean(all_gradesD)

                #Print and store the data in the txt as well as in the console
                # For Masteral
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
Minor Average: {st.mean(term1M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                print("""
============================================================
***********  End of Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
***********  End of Transcript for Level (G-M)  ************
============================================================\n""")
                
                # For Doctoral 
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
Minor Average: {st.mean(term1D)}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1D)}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term4D):.2f}       Overall Average: {ave_gradesD:.2f}""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term4D):.2f}       Overall Average: {ave_gradesD:.2f}""")
                
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

        # For Both in student level
        elif student_level == 'B':
            if _degree == 'M':
                termsM = []
                term1M = []
                term2M = []
                term3M = []
                all_gradesM = []
                termsU = []
                term1U = []
                term2U = []
                term3U = []
                term4U = []
                term5U = []
                all_gradesU = []
                # For loop that get the grades
                for row in stdStats:
                    termsU.append(int(row[2]))
                    termsM.append(int(row[2]))
                    if 'U' in row:
                        if 'Minor' in row:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                term1U.append(int(row[7]))
                            elif '2' in row[2]:
                                term2U.append(int(row[7]))
                            elif '3' in row[2]:
                                term3U.append(int(row[7]))
                            elif '4' in row[2]:
                                term4U.append(int(row[7]))
                            elif '5' in row[2]:
                                term5U.append(int(row[7]))
                    if 'M1' in row:
                        if 'Minor' in row:
                            all_gradesM.append(int(row[7]))
                            if '1' in row[2]:
                                term1M.append(int(row[7]))
                            elif '2' in row[2]:
                                term2M.append(int(row[7]))
                            elif '3' in row[2]:
                                term3M.append(int(row[7]))

                # Get the avarage in all grades
                ave_gradesM = st.mean(all_gradesM)
                ave_gradesU = st.mean(all_gradesU)
                ave_term1U = st.mean(term1U)
                ave_term2U = st.mean(term2U)
                ave_term3U = st.mean(term3U)
                ave_term4U = st.mean(term4U)
                ave_term5U = st.mean(term5U)

                #Print and store the data in the txt as well as in the console
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
Minor Average: {ave_term1U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term1U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term2U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term2U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term3U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term3U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term4U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term4U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term5U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term5U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
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
Minor Average: {st.mean(term1M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
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
            
            if _degree == 'D':
                termsD = []
                term1D = []
                term2D = []
                term3D = []
                term4D = []
                all_gradesD = []
                termsU = []
                term1U = []
                term2U = []
                term3U = []
                term4U = []
                term5U = []
                all_gradesU = []
                # For loop that get the grades
                for row in stdStats:
                    termsU.append(int(row[2]))
                    termsD.append(int(row[2]))
                    if 'U' in row:
                        if 'Minor' in row:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                term1U.append(int(row[7]))
                            elif '2' in row[2]:
                                term2U.append(int(row[7]))
                            elif '3' in row[2]:
                                term3U.append(int(row[7]))
                            elif '4' in row[2]:
                                term4U.append(int(row[7]))
                            elif '5' in row[2]:
                                term5U.append(int(row[7]))
                    if 'D1' in row:
                        if 'Minor' in row:
                            all_gradesD.append(int(row[7]))
                            if '1' in row[2]:
                                term1D.append(int(row[7]))
                            elif '2' in row[2]:
                                term2D.append(int(row[7]))
                            elif '3' in row[2]:
                                term3D.append(int(row[7]))
                            elif '4' in row[2]:
                                term4D.append(int(row[7]))

                # Get the avarage in all grades
                ave_gradesD = st.mean(all_gradesD)
                ave_gradesU = st.mean(all_gradesU)
                ave_term1U = st.mean(term1U)
                ave_term2U = st.mean(term2U)
                ave_term3U = st.mean(term3U)
                ave_term4U = st.mean(term4U)
                ave_term5U = st.mean(term5U)

                #Print and store the data in the txt as well as in the console
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
Minor Average: {ave_term1U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term1U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term2U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term2U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term3U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term3U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term4U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term4U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term5U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term5U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
                
                # For Doctoral 
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
Minor Average: {st.mean(term1D)}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1D)}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term4D):.2f}       Overall Average: {ave_gradesD:.2f}""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term4D):.2f}       Overall Average: {ave_gradesD:.2f}""")
                
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
            
            # For both in Degree
            if _degree == 'B0':
                termsM = []
                term1M = []
                term2M = []
                term3M = []
                all_gradesM = []
                termsD = []
                term1D = []
                term2D = []
                term3D = []
                term4D = []
                all_gradesD = []
                termsU = []
                term1U = []
                term2U = []
                term3U = []
                term4U = []
                term5U = []
                all_gradesU = []
                # For loop that get the grades
                for row in stdStats:
                    termsU.append(int(row[2]))
                    termsM.append(int(row[2]))
                    if 'U' in row:
                        if 'Minor' in row:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                term1U.append(int(row[7]))
                            elif '2' in row[2]:
                                term2U.append(int(row[7]))
                            elif '3' in row[2]:
                                term3U.append(int(row[7]))
                            elif '4' in row[2]:
                                term4U.append(int(row[7]))
                            elif '5' in row[2]:
                                term5U.append(int(row[7]))
                    if 'M1' in row:
                        if 'Minor' in row:
                            all_gradesM.append(int(row[7]))
                            if '1' in row[2]:
                                term1M.append(int(row[7]))
                            elif '2' in row[2]:
                                term2M.append(int(row[7]))
                            elif '3' in row[2]:
                                term3M.append(int(row[7]))
                    if 'D1' in row:
                        if 'Minor' in row:
                            all_gradesD.append(int(row[7]))
                            if '1' in row[2]:
                                term1D.append(int(row[7]))
                            elif '2' in row[2]:
                                term2D.append(int(row[7]))
                            elif '3' in row[2]:
                                term3D.append(int(row[7]))
                            elif '4' in row[2]:
                                term4D.append(int(row[7]))

                # Get the avarage in all grades
                ave_gradesD = st.mean(all_gradesD)
                ave_gradesM = st.mean(all_gradesM)
                ave_gradesU = st.mean(all_gradesU)
                ave_term1U = st.mean(term1U)
                ave_term2U = st.mean(term2U)
                ave_term3U = st.mean(term3U)
                ave_term4U = st.mean(term4U)
                ave_term5U = st.mean(term5U)

                #Print and store the data in the txt as well as in the console
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
Minor Average: {ave_term1U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term1U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term2U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term2U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term3U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term3U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term4U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term4U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term5U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {ave_term5U:.2f}       Overall Average: {ave_gradesU:.2f}\n""")
                print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================\n""")
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
Minor Average: {st.mean(term1M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3M):.2f}       Overall Average: {ave_gradesM:.2f}\n""")
                print("""
============================================================
***********  End of Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
***********  End of Transcript for Level (G-M)  ************
============================================================\n""")
                
                # For Doctoral 
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
Minor Average: {st.mean(term1D)}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term1D)}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term2D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term3D):.2f}       Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True) & (df['CourseType'].str.contains('Minor') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term4D):.2f}       Overall Average: {ave_gradesD:.2f}""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Minor Average: {st.mean(term4D):.2f}       Overall Average: {ave_gradesD:.2f}""")
                
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