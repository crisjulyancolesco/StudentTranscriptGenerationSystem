# B and B0 options for Full Transcript feature
            if _degree == 'B0':
                termsM = []
                Majterm1M = []
                Majterm2M = []
                Majterm3M = []
                Minterm1M = []
                Minterm2M = []
                Minterm3M = []
                all_gradesM = []
                termsD = []
                Majterm1D = []
                Majterm2D = []
                Majterm3D = []
                Majterm4D = []
                Minterm1D = []
                Minterm2D = []
                Minterm3D = []
                Minterm4D = []
                all_gradesD = []
                #For loop that get the grade of the student
                for row in stdStats:
                    termsM.append(int(row[2]))
                    termsD.append(int(row[2]))
                    if 'M1' in row:
                        if 'Major' in row:
                            all_gradesM.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1M.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2M.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3M.append(int(row[7]))
                        else:
                            all_gradesM.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1M.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2M.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3M.append(int(row[7]))
                    if 'D1' in row:
                        if 'Major' in row:
                            all_gradesD.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1D.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2D.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3D.append(int(row[7]))
                            elif '4' in row[2]:
                                Majterm4D.append(int(row[7]))
                        else:
                            all_gradesD.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1D.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2D.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3D.append(int(row[7]))
                            elif '4' in row[2]:
                                Minterm4D.append(int(row[7]))

                # Get the overall average and the average each term
                ave_gradesM = st.mean(all_gradesM)
                ave_Majterm1M = st.mean(Majterm1M)
                ave_Majterm2M = st.mean(Majterm2M)
                ave_Majterm3M = st.mean(Majterm3M)
                ave_Minterm1M = st.mean(Minterm1M)
                ave_Minterm2M = st.mean(Minterm2M)
                ave_Minterm3M = st.mean(Minterm3M)
                ave_gradesD = st.mean(all_gradesD)
                ave_Majterm1D = st.mean(Majterm1D)
                ave_Majterm2D = st.mean(Majterm2D)
                ave_Majterm3D = st.mean(Majterm3D)
                ave_Majterm4D = st.mean(Majterm4D)
                ave_Minterm1D = st.mean(Minterm1D)
                ave_Minterm2D = st.mean(Minterm2D)
                ave_Minterm3D = st.mean(Minterm3D)
                ave_Minterm4D = st.mean(Minterm4D)

                # Print and store the data in the txt file
                print("""
============================================================
*************  Full Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (G-M)  ************
============================================================\n""")
                # For Masteral
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1M:.2f}       Minor Average: {ave_Minterm1M:.2f} 
Term Average: {st.mean(Majterm1M + Minterm1M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1M:.2f}       Minor Average: {ave_Minterm1M:.2f} 
Term Average: {st.mean(Majterm1M + Minterm1M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2M:.2f}       Minor Average: {ave_Minterm2M:.2f}   
Term Average: {st.mean(Majterm2M + Minterm2M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2M:.2f}       Minor Average: {ave_Minterm2M:.2f}   
Term Average: {st.mean(Majterm2M + Minterm2M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3M:.2f}       Minor Average: {ave_Minterm3M:.2f}  
Term Average: {st.mean(Majterm3M + Minterm3M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3M:.2f}       Minor Average: {ave_Minterm3M:.2f}  
Term Average: {st.mean(Majterm3M + Minterm3M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                print("""
============================================================
************  End of Transcript for Level (G-M)  ***********
============================================================\n""")
                myFile.write("""
============================================================
************  End of Transcript for Level (G-M)  ***********
============================================================\n""")
                
                # For Doctoral
                print("""
============================================================
*************  Full Transcript for Level (G-D)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (G-D)  ************
============================================================\n""")
                # For Doctoral
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1D:.2f}       Minor Average: {ave_Minterm1D:.2f} 
Term Average: {st.mean(Majterm1D + Minterm1D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1D:.2f}       Minor Average: {ave_Minterm1D:.2f} 
Term Average: {st.mean(Majterm1D + Minterm1D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2D:.2f}       Minor Average: {ave_Minterm2D:.2f}   
Term Average: {st.mean(Majterm2D + Minterm2D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2D:.2f}       Minor Average: {ave_Minterm2D:.2f}   
Term Average: {st.mean(Majterm2D + Minterm2D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3D:.2f}       Minor Average: {ave_Minterm3D:.2f}  
Term Average: {st.mean(Majterm3D + Minterm3D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3D:.2f}       Minor Average: {ave_Minterm3D:.2f}  
Term Average: {st.mean(Majterm3D + Minterm3D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4D:.2f}       Minor Average: {ave_Minterm4D:.2f}  
Term Average: {st.mean(Majterm4D + Minterm4D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4D:.2f}       Minor Average: {ave_Minterm4D:.2f}  
Term Average: {st.mean(Majterm4D + Minterm4D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
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
        
        #For Both in student level
        elif student_level == 'B':
            if _degree == 'M':
                termsU = []
                Majterm1U = []
                Majterm2U = []
                Majterm3U = []
                Majterm4U = []
                Majterm5U = []
                Minterm1U = []
                Minterm2U = []
                Minterm3U = []
                Minterm4U = []
                Minterm5U = []
                all_gradesU = []
                termsM = []
                Majterm1M = []
                Majterm2M = []
                Majterm3M = []
                Minterm1M = []
                Minterm2M = []
                Minterm3M = []
                all_gradesM = []
                #For loop that get the grade of the student
                for row in stdStats:
                    termsU.append(int(row[2]))
                    termsM.append(int(row[2]))
                    if 'M1' in row:
                        if 'Major' in row:
                            all_gradesM.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1M.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2M.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3M.append(int(row[7]))
                        else:
                            all_gradesM.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1M.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2M.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3M.append(int(row[7]))
                    elif 'U' in row:
                        if 'Major' in row:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1U.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2U.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3U.append(int(row[7]))
                            elif '4' in row[2]:
                                Majterm4U.append(int(row[7]))
                            elif '5' in row[2]:
                                Majterm5U.append(int(row[7]))
                        else:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1U.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2U.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3U.append(int(row[7]))
                            elif '4' in row[2]:
                                Minterm4U.append(int(row[7]))
                            elif '5' in row[2]:
                                Minterm5U.append(int(row[7]))

                # Get the overall average and the average each term
                ave_gradesM = st.mean(all_gradesM)
                ave_Majterm1M = st.mean(Majterm1M)
                ave_Majterm2M = st.mean(Majterm2M)
                ave_Majterm3M = st.mean(Majterm3M)
                ave_Minterm1M = st.mean(Minterm1M)
                ave_Minterm2M = st.mean(Minterm2M)
                ave_Minterm3M = st.mean(Minterm3M)
                ave_gradesU = st.mean(all_gradesU)
                ave_Majterm1U = st.mean(Majterm1U)
                ave_Majterm2U = st.mean(Majterm2U)
                ave_Majterm3U = st.mean(Majterm3U)
                ave_Majterm4U = st.mean(Majterm4U)
                ave_Majterm5U = st.mean(Majterm5U)
                ave_Minterm1U = st.mean(Minterm1U)
                ave_Minterm2U = st.mean(Minterm2U)
                ave_Minterm3U = st.mean(Minterm3U)
                ave_Minterm4U = st.mean(Minterm4U)
                ave_Minterm5U = st.mean(Minterm5U)

                # Print and store the data in the txt file
                print("""
============================================================
*************  Full Transcript for Level (U)  **************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (U)  **************
============================================================\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 1  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1U:.2f}       Minor Average: {ave_Minterm1U:.2f} 
Term Average: {st.mean(Majterm1U + Minterm1U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 1  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1U:.2f}       Minor Average: {ave_Minterm1U:.2f} 
Term Average: {st.mean(Majterm1U + Minterm1U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
            
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2U:.2f}       Minor Average: {ave_Minterm2U:.2f}   
Term Average: {st.mean(Majterm2U + Minterm2U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2U:.2f}       Minor Average: {ave_Minterm2U:.2f}   
Term Average: {st.mean(Majterm2U + Minterm2U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 3  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3U:.2f}       Minor Average: {ave_Minterm3U:.2f}  
Term Average: {st.mean(Majterm3U + Minterm3U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3U:.2f}       Minor Average: {ave_Minterm3U:.2f}  
Term Average: {st.mean(Majterm3U + Minterm3U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4U:.2f}       Minor Average: {ave_Minterm4U:.2f}  
Term Average: {st.mean(Majterm4U + Minterm4U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4U:.2f}       Minor Average: {ave_Minterm4U:.2f}  
Term Average: {st.mean(Majterm4U + Minterm4U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm5U:.2f}       Minor Average: {ave_Minterm5U:.2f}  
Term Average: {st.mean(Majterm5U + Minterm5U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm5U:.2f}       Minor Average: {ave_Minterm5U:.2f}  
Term Average: {st.mean(Majterm5U + Minterm5U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================""")
                myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================""")

                # For Masteral
                print("""
============================================================
*************  Full Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (G-M)  ************
============================================================\n""")
                # For Masteral
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1M:.2f}       Minor Average: {ave_Minterm1M:.2f} 
Term Average: {st.mean(Majterm1M + Minterm1M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1M:.2f}       Minor Average: {ave_Minterm1M:.2f} 
Term Average: {st.mean(Majterm1M + Minterm1M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2M:.2f}       Minor Average: {ave_Minterm2M:.2f}   
Term Average: {st.mean(Majterm2M + Minterm2M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2M:.2f}       Minor Average: {ave_Minterm2M:.2f}   
Term Average: {st.mean(Majterm2M + Minterm2M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3M:.2f}       Minor Average: {ave_Minterm3M:.2f}  
Term Average: {st.mean(Majterm3M + Minterm3M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3M:.2f}       Minor Average: {ave_Minterm3M:.2f}  
Term Average: {st.mean(Majterm3M + Minterm3M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
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
            
            elif _degree == 'D':
                termsU = []
                Majterm1U = []
                Majterm2U = []
                Majterm3U = []
                Majterm4U = []
                Majterm5U = []
                Minterm1U = []
                Minterm2U = []
                Minterm3U = []
                Minterm4U = []
                Minterm5U = []
                all_gradesU = []
                termsD = []
                Majterm1D = []
                Majterm2D = []
                Majterm3D = []
                Majterm4D = []
                Minterm1D = []
                Minterm2D = []
                Minterm3D = []
                Minterm4D = []
                all_gradesD = []
                #For loop that get the grades of the student
                for row in stdStats:
                    termsU.append(int(row[2]))
                    if 'U' in row:
                        if 'Major' in row:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1U.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2U.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3U.append(int(row[7]))
                            elif '4' in row[2]:
                                Majterm4U.append(int(row[7]))
                            elif '5' in row[2]:
                                Majterm5U.append(int(row[7]))
                        else:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1U.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2U.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3U.append(int(row[7]))
                            elif '4' in row[2]:
                                Minterm4U.append(int(row[7]))
                            elif '5' in row[2]:
                                Minterm5U.append(int(row[7]))
                    elif 'D1' in row:
                        if 'Major' in row:
                            all_gradesD.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1D.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2D.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3D.append(int(row[7]))
                            elif '4' in row[2]:
                                Majterm4D.append(int(row[7]))
                        else:
                            all_gradesD.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1D.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2D.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3D.append(int(row[7]))
                            elif '4' in row[2]:
                                Minterm4D.append(int(row[7]))

                # Get the overall average as well as the average in each term
                ave_gradesU = st.mean(all_gradesU)
                ave_Majterm1U = st.mean(Majterm1U)
                ave_Majterm2U = st.mean(Majterm2U)
                ave_Majterm3U = st.mean(Majterm3U)
                ave_Majterm4U = st.mean(Majterm4U)
                ave_Majterm5U = st.mean(Majterm5U)
                ave_Minterm1U = st.mean(Minterm1U)
                ave_Minterm2U = st.mean(Minterm2U)
                ave_Minterm3U = st.mean(Minterm3U)
                ave_Minterm4U = st.mean(Minterm4U)
                ave_Minterm5U = st.mean(Minterm5U)
                ave_gradesD = st.mean(all_gradesD)
                ave_Majterm1D = st.mean(Majterm1D)
                ave_Majterm2D = st.mean(Majterm2D)
                ave_Majterm3D = st.mean(Majterm3D)
                ave_Majterm4D = st.mean(Majterm4D)
                ave_Minterm1D = st.mean(Minterm1D)
                ave_Minterm2D = st.mean(Minterm2D)
                ave_Minterm3D = st.mean(Minterm3D)
                ave_Minterm4D = st.mean(Minterm4D)

            # Print and store the grades in the txt file
                print("""
============================================================
*************  Full Transcript for Level (U)  **************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (U)  **************
============================================================\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 1  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1U:.2f}       Minor Average: {ave_Minterm1U:.2f} 
Term Average: {st.mean(Majterm1U + Minterm1U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 1  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1U:.2f}       Minor Average: {ave_Minterm1U:.2f} 
Term Average: {st.mean(Majterm1U + Minterm1U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
            
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2U:.2f}       Minor Average: {ave_Minterm2U:.2f}   
Term Average: {st.mean(Majterm2U + Minterm2U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2U:.2f}       Minor Average: {ave_Minterm2U:.2f}   
Term Average: {st.mean(Majterm2U + Minterm2U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 3  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3U:.2f}       Minor Average: {ave_Minterm3U:.2f}  
Term Average: {st.mean(Majterm3U + Minterm3U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3U:.2f}       Minor Average: {ave_Minterm3U:.2f}  
Term Average: {st.mean(Majterm3U + Minterm3U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4U:.2f}       Minor Average: {ave_Minterm4U:.2f}  
Term Average: {st.mean(Majterm4U + Minterm4U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4U:.2f}       Minor Average: {ave_Minterm4U:.2f}  
Term Average: {st.mean(Majterm4U + Minterm4U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm5U:.2f}       Minor Average: {ave_Minterm5U:.2f}  
Term Average: {st.mean(Majterm5U + Minterm5U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm5U:.2f}       Minor Average: {ave_Minterm5U:.2f}  
Term Average: {st.mean(Majterm5U + Minterm5U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================""")
                myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================""")
                
                # For Doctoral
                print("""
============================================================
*************  Full Transcript for Level (G-D)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (G-D)  ************
============================================================\n""")
                # For Doctoral
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1D:.2f}       Minor Average: {ave_Minterm1D:.2f} 
Term Average: {st.mean(Majterm1D + Minterm1D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1D:.2f}       Minor Average: {ave_Minterm1D:.2f} 
Term Average: {st.mean(Majterm1D + Minterm1D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2D:.2f}       Minor Average: {ave_Minterm2D:.2f}   
Term Average: {st.mean(Majterm2D + Minterm2D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2D:.2f}       Minor Average: {ave_Minterm2D:.2f}   
Term Average: {st.mean(Majterm2D + Minterm2D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3D:.2f}       Minor Average: {ave_Minterm3D:.2f}  
Term Average: {st.mean(Majterm3D + Minterm3D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3D:.2f}       Minor Average: {ave_Minterm3D:.2f}  
Term Average: {st.mean(Majterm3D + Minterm3D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4D:.2f}       Minor Average: {ave_Minterm4D:.2f}  
Term Average: {st.mean(Majterm4D + Minterm4D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4D:.2f}       Minor Average: {ave_Minterm4D:.2f}  
Term Average: {st.mean(Majterm4D + Minterm4D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
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
            
            # For both in degree
            elif _degree == 'B0':
                termsU = []
                Majterm1U = []
                Majterm2U = []
                Majterm3U = []
                Majterm4U = []
                Majterm5U = []
                Minterm1U = []
                Minterm2U = []
                Minterm3U = []
                Minterm4U = []
                Minterm5U = []
                all_gradesU = []
                termsM = []
                Majterm1M = []
                Majterm2M = []
                Majterm3M = []
                Minterm1M = []
                Minterm2M = []
                Minterm3M = []
                all_gradesM = []
                termsD = []
                Majterm1D = []
                Majterm2D = []
                Majterm3D = []
                Majterm4D = []
                Minterm1D = []
                Minterm2D = []
                Minterm3D = []
                Minterm4D = []
                all_gradesD = []
                #For loop that get the grade of the student
                for row in stdStats:
                    termsU.append(int(row[2]))
                    termsM.append(int(row[2]))
                    if 'M1' in row:
                        if 'Major' in row:
                            all_gradesM.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1M.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2M.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3M.append(int(row[7]))
                        else:
                            all_gradesM.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1M.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2M.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3M.append(int(row[7]))
                    elif 'U' in row:
                        if 'Major' in row:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1U.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2U.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3U.append(int(row[7]))
                            elif '4' in row[2]:
                                Majterm4U.append(int(row[7]))
                            elif '5' in row[2]:
                                Majterm5U.append(int(row[7]))
                        else:
                            all_gradesU.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1U.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2U.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3U.append(int(row[7]))
                            elif '4' in row[2]:
                                Minterm4U.append(int(row[7]))
                            elif '5' in row[2]:
                                Minterm5U.append(int(row[7]))
                    elif 'D1' in row:
                        if 'Major' in row:
                            all_gradesD.append(int(row[7]))
                            if '1' in row[2]:
                                Majterm1D.append(int(row[7]))
                            elif '2' in row[2]:
                                Majterm2D.append(int(row[7]))
                            elif '3' in row[2]:
                                Majterm3D.append(int(row[7]))
                            elif '4' in row[2]:
                                Majterm4D.append(int(row[7]))
                        else:
                            all_gradesD.append(int(row[7]))
                            if '1' in row[2]:
                                Minterm1D.append(int(row[7]))
                            elif '2' in row[2]:
                                Minterm2D.append(int(row[7]))
                            elif '3' in row[2]:
                                Minterm3D.append(int(row[7]))
                            elif '4' in row[2]:
                                Minterm4D.append(int(row[7]))

                # Get the overall average and the average each term
                ave_gradesM = st.mean(all_gradesM)
                ave_Majterm1M = st.mean(Majterm1M)
                ave_Majterm2M = st.mean(Majterm2M)
                ave_Majterm3M = st.mean(Majterm3M)
                ave_Minterm1M = st.mean(Minterm1M)
                ave_Minterm2M = st.mean(Minterm2M)
                ave_Minterm3M = st.mean(Minterm3M)
                ave_gradesU = st.mean(all_gradesU)
                ave_Majterm1U = st.mean(Majterm1U)
                ave_Majterm2U = st.mean(Majterm2U)
                ave_Majterm3U = st.mean(Majterm3U)
                ave_Majterm4U = st.mean(Majterm4U)
                ave_Majterm5U = st.mean(Majterm5U)
                ave_Minterm1U = st.mean(Minterm1U)
                ave_Minterm2U = st.mean(Minterm2U)
                ave_Minterm3U = st.mean(Minterm3U)
                ave_Minterm4U = st.mean(Minterm4U)
                ave_Minterm5U = st.mean(Minterm5U)
                ave_gradesD = st.mean(all_gradesD)
                ave_Majterm1D = st.mean(Majterm1D)
                ave_Majterm2D = st.mean(Majterm2D)
                ave_Majterm3D = st.mean(Majterm3D)
                ave_Majterm4D = st.mean(Majterm4D)
                ave_Minterm1D = st.mean(Minterm1D)
                ave_Minterm2D = st.mean(Minterm2D)
                ave_Minterm3D = st.mean(Minterm3D)
                ave_Minterm4D = st.mean(Minterm4D)

                # Print and store the data in the txt file
                print("""
============================================================
*************  Full Transcript for Level (U)  **************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (U)  **************
============================================================\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 1  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1U:.2f}       Minor Average: {ave_Minterm1U:.2f} 
Term Average: {st.mean(Majterm1U + Minterm1U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 1  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1U:.2f}       Minor Average: {ave_Minterm1U:.2f} 
Term Average: {st.mean(Majterm1U + Minterm1U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
            
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2U:.2f}       Minor Average: {ave_Minterm2U:.2f}   
Term Average: {st.mean(Majterm2U + Minterm2U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2U:.2f}       Minor Average: {ave_Minterm2U:.2f}   
Term Average: {st.mean(Majterm2U + Minterm2U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 3  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3U:.2f}       Minor Average: {ave_Minterm3U:.2f}  
Term Average: {st.mean(Majterm3U + Minterm3U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3U:.2f}       Minor Average: {ave_Minterm3U:.2f}  
Term Average: {st.mean(Majterm3U + Minterm3U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4U:.2f}       Minor Average: {ave_Minterm4U:.2f}  
Term Average: {st.mean(Majterm4U + Minterm4U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4U:.2f}       Minor Average: {ave_Minterm4U:.2f}  
Term Average: {st.mean(Majterm4U + Minterm4U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 5) & (df['Level'].str.contains('U') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm5U:.2f}       Minor Average: {ave_Minterm5U:.2f}  
Term Average: {st.mean(Majterm5U + Minterm5U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 5  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm5U:.2f}       Minor Average: {ave_Minterm5U:.2f}  
Term Average: {st.mean(Majterm5U + Minterm5U):.2f}        Overall Average: {ave_gradesU:.2f}\n""")
                print("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================""")
                myFile.write("""
============================================================
*************  End of Transcript for Level (U)  ************
============================================================""")

                # For Masteral
                print("""
============================================================
*************  Full Transcript for Level (G-M)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (G-M)  ************
============================================================\n""")
                # For Masteral
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1M:.2f}       Minor Average: {ave_Minterm1M:.2f} 
Term Average: {st.mean(Majterm1M + Minterm1M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1M:.2f}       Minor Average: {ave_Minterm1M:.2f} 
Term Average: {st.mean(Majterm1M + Minterm1M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 2  ***************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2M:.2f}       Minor Average: {ave_Minterm2M:.2f}   
Term Average: {st.mean(Majterm2M + Minterm2M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2M:.2f}       Minor Average: {ave_Minterm2M:.2f}   
Term Average: {st.mean(Majterm2M + Minterm2M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('M1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3M:.2f}       Minor Average: {ave_Minterm3M:.2f}  
Term Average: {st.mean(Majterm3M + Minterm3M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3M:.2f}       Minor Average: {ave_Minterm3M:.2f}  
Term Average: {st.mean(Majterm3M + Minterm3M):.2f}            Overall Average: {ave_gradesM:.2f}\n""")
                print("""
============================================================
************  End of Transcript for Level (G-M)  ***********
============================================================\n""")
                myFile.write("""
============================================================
************  End of Transcript for Level (G-M)  ***********
============================================================\n""")
                
                #For Doctoral
                print("""
============================================================
*************  Full Transcript for Level (G-D)  ************
============================================================\n""")
                myFile.write("""
============================================================
*************  Full Transcript for Level (G-D)  ************
============================================================\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 1) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1D:.2f}       Minor Average: {ave_Minterm1D:.2f} 
Term Average: {st.mean(Majterm1D + Minterm1D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 1  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm1D:.2f}       Minor Average: {ave_Minterm1D:.2f} 
Term Average: {st.mean(Majterm1D + Minterm1D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 2) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2D:.2f}       Minor Average: {ave_Minterm2D:.2f}   
Term Average: {st.mean(Majterm2D + Minterm2D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
************************  Term 2  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm2D:.2f}       Minor Average: {ave_Minterm2D:.2f}   
Term Average: {st.mean(Majterm2D + Minterm2D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")

                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 3) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3D:.2f}       Minor Average: {ave_Minterm3D:.2f}  
Term Average: {st.mean(Majterm3D + Minterm3D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 3  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm3D:.2f}       Minor Average: {ave_Minterm3D:.2f}  
Term Average: {st.mean(Majterm3D + Minterm3D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                
                df = pd.read_csv(f"{stdID}.csv")
                df = df[(df['Term'] == 4) & (df['Degree'].str.contains('D1') == True)].set_index(['Level'])
                print(f"""
============================================================
***********************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4D:.2f}       Minor Average: {ave_Minterm4D:.2f}  
Term Average: {st.mean(Majterm4D + Minterm4D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
                myFile.write(f"""
============================================================
***********************  Term 4  **************************
============================================================
{df[['CourseID', 'CourseName', 'CreditHours', 'Grade']]}
Major Average: {ave_Majterm4D:.2f}       Minor Average: {ave_Minterm4D:.2f}  
Term Average: {st.mean(Majterm4D + Minterm4D):.2f}            Overall Average: {ave_gradesD:.2f}\n""")
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