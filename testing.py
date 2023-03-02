# B and B0 options for Statistics feature
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
                # For loop that will store the grades of the student.
                for row in stdStats:
                    termsM.append(int(row[2]))
                    termsD.append(int(row[2]))
                    if 'M1' in row[1]:
                        all_gradesM.append(int(row[7]))
                        if '1' in row[2]:
                            term1M.append(int(row[7]))
                        elif '2' in row[2]:
                            term2M.append(int(row[7]))
                        elif '3' in row[2]:
                            term3M.append(int(row[7]))
                    if 'D1' in row[1]:
                        all_gradesD.append(int(row[7]))
                        if '1' in row[2]:
                            term1D.append(int(row[7]))
                        elif '2' in row[2]:
                            term2D.append(int(row[7]))
                        elif '3' in row[2]:
                            term3D.append(int(row[7]))
                        elif '4' in row[2]:
                            term4D.append(int(row[7]))

                # Get the overall average as well as the average in each term.
                ave_gradesM = st.mean(all_gradesM)
                ave_term1M = st.mean(term1M)
                ave_term2M = st.mean(term2M)
                ave_term3M = st.mean(term3M)
                ave_gradesD = st.mean(all_gradesD)
                ave_term1D = st.mean(term1D)
                ave_term2D = st.mean(term2D)
                ave_term3D = st.mean(term3D)
                ave_term4D = st.mean(term4D)

                # Check the maximum grade and in what term.
                max_gradesM = int(max(all_gradesM))
                for gtM in range(len(all_gradesM)):
                    grade_M = int(all_gradesM[gtM])
                    if grade_M == max_gradesM:
                        max_grades_termM = termsM[gtM]
                        break
                
                # Check the minimum grade and in what term.
                min_gradesM = int(min(all_gradesM))
                for gtM in range(len(all_gradesM)):
                    grade_M = int(all_gradesM[gtM])
                    if grade_M == min_gradesM:
                        min_grades_termM = termsM[gtM]
                        break

                # Check the maximum grade and in what term.
                max_gradesD = int(max(all_gradesD))
                for gtD in range(len(all_gradesD)):
                    grade_D = int(all_gradesD[gtD])
                    if grade_D == max_gradesD:
                        max_grades_termD = termsM[gtD]
                        break
                
                # Check the minimum grade and in what term.
                min_gradesD = int(min(all_gradesD))
                for gtD in range(len(all_gradesD)):
                    grade_D = int(all_gradesD[gtD])
                    if grade_D == min_gradesD:
                        min_grades_termD = termsM[gtD]
                        break
                
                # Print the Statistic data in the console.
                print(f"""
============================================================
******************** Graduate(M) Level *********************
============================================================
Overall average (major and minor) for all terms: {ave_gradesM:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1M:.2f}
\t Term 2: {ave_term2M:.2f}
\t Term 3: {ave_term3M:.2f}
Maximum grade(s) and in which terms(s): {max_gradesM:.2f} in Term: {max_grades_termM}
Minimum grade(s) and in which term(s): {min_gradesM:.2f} in Term: {min_grades_termM}
Do you have any repeated course(s)? None\n""")
                print(f"""
============================================================
******************\t Graduate(D) Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_gradesD:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1D:.2f}
\t Term 2: {ave_term2D:.2f}
\t Term 3: {ave_term3D:.2f}
\t Term 4: {ave_term4D:.2f}
Maximum grade(s) and in which terms(s): {max_gradesD:.2f} in Term: {max_grades_termD}
Minimum grade(s) and in which term(s): {min_gradesD:.2f} in Term: {min_grades_termD}
Do you have any repeated course(s)? None""")

            # Create a txt file
                filename = "std" + stdID + "statistics.txt"
                myFile = open(filename, 'w')
                # Stores the Data in the txt file
                myFile.write(f"""============================================================
*****************\t Graduate(M) Level\t *****************
============================================================
Overall average (major and minor) for all terms: {ave_gradesM:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1M:.2f}
\t Term 2: {ave_term2M:.2f}
\t Term 3: {ave_term3M:.2f}
Maximum grade(s) and in which terms(s): {max_gradesM:.2f} in Term: {max_grades_termM}
Minimum grade(s) and in which term(s): {min_gradesM:.2f} in Term: {min_grades_termM}
Do you have any repeated course(s)? None\n""")
                myFile.write(f"""
============================================================
******************\t Graduate(D) Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_gradesD:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1D:.2f}
\t Term 2: {ave_term2D:.2f}
\t Term 3: {ave_term3D:.2f}
\t Term 4: {ave_term4D:.2f}
Maximum grade(s) and in which terms(s): {max_gradesD:.2f} in Term: {max_grades_termD}
Minimum grade(s) and in which term(s): {min_gradesD:.2f} in Term: {min_grades_termD}
Do you have any repeated course(s)? None """)
                
                # Open the txt file.
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)
        
        # For Both
        elif student_level == 'B':
            # Master
            if _degree == 'M':
                termsU = []
                term1U = []
                term2U = []
                term3U = []
                term4U = []
                term5U = []
                all_gradesU = []
                terms = []
                term1 = []
                term2 = []
                term3 = []
                all_grades = []
                # For loop that will store the grades of the student.
                for row in stdStats:
                    termsU.append(int(row[2]))
                    terms.append(int(row[2]))
                    if 'U' in row:
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
                    if 'M1' in row[1]:
                        all_grades.append(int(row[7]))
                        if '1' in row[2]:
                            term1.append(int(row[7]))
                        elif '2' in row[2]:
                            term2.append(int(row[7]))
                        elif '3' in row[2]:
                            term3.append(int(row[7]))
                
                # Get the overall average as well as the average in each term.
                ave_gradesU = st.mean(all_gradesU)
                ave_term1U = st.mean(term1U)
                ave_term2U = st.mean(term2U)
                ave_term3U = st.mean(term3U)
                ave_term4U = st.mean(term4U)
                ave_term5U = st.mean(term5U)
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
                
                    # Check the maximum grade and in what term.
                max_gradesU = int(max(all_gradesU))
                for gtU in range(len(all_gradesU)):
                    grade_U = int(all_gradesU[gtU])
                    if grade_U == max_gradesU:
                        max_grades_termU = termsU[gtU]
                        break
                
                # Check the minimum grade and in what term.
                min_gradesU = int(min(all_gradesU))
                for gtU in range(len(all_gradesU)):
                    grade_U = int(all_gradesU[gtU])
                    if grade_U == min_gradesU:
                        min_grades_termU = termsU[gtU]
                        break

                # Print the Statistic data in the console.
                print(f"""============================================================
*****************\t Undergraduate Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_gradesU:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1U:.2f}
\t Term 2: {ave_term2U:.2f}
\t Term 3: {ave_term3U:.2f}
\t Term 4: {ave_term4U:.2f}
\t Term 5: {ave_term5U:.2f}
Maximum grade(s) and in which terms(s): {max_gradesU:.2f} in Term: {max_grades_termU}
Minimum grade(s) and in which term(s): {min_gradesU:.2f} in Term: {min_grades_termU}
Do you have any repeated course(s)? None\n""")
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
****************\t Undergraduate Level\t ****************
============================================================
Overall average (major and minor) for all terms: {ave_gradesU:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1U:.2f}
\t Term 2: {ave_term2U:.2f}
\t Term 3: {ave_term3U:.2f}
\t Term 4: {ave_term4U:.2f}
\t Term 5: {ave_term5U:.2f}
Maximum grade(s) and in which terms(s): {max_gradesU:.2f} in Term: {max_grades_termU}
Minimum grade(s) and in which term(s): {min_gradesU:.2f} in Term: {min_grades_termU}
Do you have any repeated course(s)? None\n""")
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
                termsU = []
                term1U = []
                term2U = []
                term3U = []
                term4U = []
                term5U = []
                all_gradesU = []
                terms = []
                term1 = []
                term2 = []
                term3 = []
                term4 = []
                all_grades = []
                # For loop that get the grade of the graduate student.
                for row in stdStats:
                    termsU.append(int(row[2]))
                    terms.append(int(row[2]))
                    if 'U' in row:
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
                ave_gradesU = st.mean(all_gradesU)
                ave_term1U = st.mean(term1U)
                ave_term2U = st.mean(term2U)
                ave_term3U = st.mean(term3U)
                ave_term4U = st.mean(term4U)
                ave_term5U = st.mean(term5U)
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
                
                # Check the maximum grade and in what term.
                max_gradesU = int(max(all_gradesU))
                for gtU in range(len(all_gradesU)):
                    grade_U = int(all_gradesU[gtU])
                    if grade_U == max_gradesU:
                        max_grades_termU = termsU[gtU]
                        break
                
                # Check the minimum grade and in what term.
                min_gradesU = int(min(all_gradesU))
                for gtU in range(len(all_gradesU)):
                    grade_U = int(all_gradesU[gtU])
                    if grade_U == min_gradesU:
                        min_grades_termU = termsU[gtU]
                        break
                
                # Print the statistic Data.
                print(f"""============================================================
*****************\t Undergraduate Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_gradesU:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1U:.2f}
\t Term 2: {ave_term2U:.2f}
\t Term 3: {ave_term3U:.2f}
\t Term 4: {ave_term4U:.2f}
\t Term 5: {ave_term5U:.2f}
Maximum grade(s) and in which terms(s): {max_gradesU:.2f} in Term: {max_grades_termU}
Minimum grade(s) and in which term(s): {min_gradesU:.2f} in Term: {min_grades_termU}
Do you have any repeated course(s)? None\n""")
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
                # Stores the Data in the txt file
                myFile.write(f"""============================================================
****************\t Undergraduate Level\t ****************
============================================================
Overall average (major and minor) for all terms: {ave_gradesU:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1U:.2f}
\t Term 2: {ave_term2U:.2f}
\t Term 3: {ave_term3U:.2f}
\t Term 4: {ave_term4U:.2f}
\t Term 5: {ave_term5U:.2f}
Maximum grade(s) and in which terms(s): {max_gradesU:.2f} in Term: {max_grades_termU}
Minimum grade(s) and in which term(s): {min_gradesU:.2f} in Term: {min_grades_termU}
Do you have any repeated course(s)? None\n""")
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
                termsU = []
                term1U = []
                term2U = []
                term3U = []
                term4U = []
                term5U = []
                all_gradesU = []
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
                # For loop that will store the grades of the student.
                for row in stdStats:
                    termsU.append(int(row[2]))
                    termsM.append(int(row[2]))
                    termsD.append(int(row[2]))
                    if 'U' in row:
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
                    if 'M1' in row[1]:
                        all_gradesM.append(int(row[7]))
                        if '1' in row[2]:
                            term1M.append(int(row[7]))
                        elif '2' in row[2]:
                            term2M.append(int(row[7]))
                        elif '3' in row[2]:
                            term3M.append(int(row[7]))
                    elif 'D1' in row[1]:
                        all_gradesD.append(int(row[7]))
                        if '1' in row[2]:
                            term1D.append(int(row[7]))
                        elif '2' in row[2]:
                            term2D.append(int(row[7]))
                        elif '3' in row[2]:
                            term3D.append(int(row[7]))
                        elif '4' in row[2]:
                            term4D.append(int(row[7]))

                # Get the overall average as well as the average in each term.
                ave_gradesU = st.mean(all_gradesU)
                ave_term1U = st.mean(term1U)
                ave_term2U = st.mean(term2U)
                ave_term3U = st.mean(term3U)
                ave_term4U = st.mean(term4U)
                ave_term5U = st.mean(term5U)
                ave_gradesM = st.mean(all_gradesM)
                ave_term1M = st.mean(term1M)
                ave_term2M = st.mean(term2M)
                ave_term3M = st.mean(term3M)
                ave_gradesD = st.mean(all_gradesD)
                ave_term1D = st.mean(term1D)
                ave_term2D = st.mean(term2D)
                ave_term3D = st.mean(term3D)
                ave_term4D = st.mean(term4D)

                # Check the maximum grade and in what term.
                max_gradesM = int(max(all_gradesM))
                for gtM in range(len(all_gradesM)):
                    grade_M = int(all_gradesM[gtM])
                    if grade_M == max_gradesM:
                        max_grades_termM = termsM[gtM]
                        break
                
                # Check the minimum grade and in what term.
                min_gradesM = int(min(all_gradesM))
                for gtM in range(len(all_gradesM)):
                    grade_M = int(all_gradesM[gtM])
                    if grade_M == min_gradesM:
                        min_grades_termM = termsM[gtM]
                        break

                # Check the maximum grade and in what term.
                max_gradesD = int(max(all_gradesD))
                for gtD in range(len(all_gradesD)):
                    grade_D = int(all_gradesD[gtD])
                    if grade_D == max_gradesD:
                        max_grades_termD = termsM[gtD]
                        break
                
                # Check the minimum grade and in what term.
                min_gradesD = int(min(all_gradesD))
                for gtD in range(len(all_gradesD)):
                    grade_D = int(all_gradesD[gtD])
                    if grade_D == min_gradesD:
                        min_grades_termD = termsM[gtD]
                        break
                
                # Check the maximum grade and in what term.
                max_gradesU = int(max(all_gradesU))
                for gtU in range(len(all_gradesU)):
                    grade_U = int(all_gradesU[gtU])
                    if grade_U == max_gradesU:
                        max_grades_termU = termsU[gtU]
                        break
                
                # Check the minimum grade and in what term.
                min_gradesU = int(min(all_gradesU))
                for gtU in range(len(all_gradesU)):
                    grade_U = int(all_gradesU[gtU])
                    if grade_U == min_gradesU:
                        min_grades_termU = termsU[gtU]
                        break
                
                # Print the Statistic data in the console.
                print(f"""============================================================
*****************\t Undergraduate Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_gradesU:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1U:.2f}
\t Term 2: {ave_term2U:.2f}
\t Term 3: {ave_term3U:.2f}
\t Term 4: {ave_term4U:.2f}
\t Term 5: {ave_term5U:.2f}
Maximum grade(s) and in which terms(s): {max_gradesU:.2f} in Term: {max_grades_termU}
Minimum grade(s) and in which term(s): {min_gradesU:.2f} in Term: {min_grades_termU}
Do you have any repeated course(s)? None\n""")
                print(f"""
============================================================
******************** Graduate(M) Level *********************
============================================================
Overall average (major and minor) for all terms: {ave_gradesM:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1M:.2f}
\t Term 2: {ave_term2M:.2f}
\t Term 3: {ave_term3M:.2f}
Maximum grade(s) and in which terms(s): {max_gradesM:.2f} in Term: {max_grades_termM}
Minimum grade(s) and in which term(s): {min_gradesM:.2f} in Term: {min_grades_termM}
Do you have any repeated course(s)? None\n""")
                print(f"""
============================================================
******************\t Graduate(D) Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_gradesD:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1D:.2f}
\t Term 2: {ave_term2D:.2f}
\t Term 3: {ave_term3D:.2f}
\t Term 4: {ave_term4D:.2f}
Maximum grade(s) and in which terms(s): {max_gradesD:.2f} in Term: {max_grades_termD}
Minimum grade(s) and in which term(s): {min_gradesD:.2f} in Term: {min_grades_termD}
Do you have any repeated course(s)? None""")

            # Create a txt file
                filename = "std" + stdID + "statistics.txt"
                myFile = open(filename, 'w')
                # Stores the Data in the txt file
                myFile.write(f"""============================================================
****************\t Undergraduate Level\t ****************
============================================================
Overall average (major and minor) for all terms: {ave_gradesU:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1U:.2f}
\t Term 2: {ave_term2U:.2f}
\t Term 3: {ave_term3U:.2f}
\t Term 4: {ave_term4U:.2f}
\t Term 5: {ave_term5U:.2f}
Maximum grade(s) and in which terms(s): {max_gradesU:.2f} in Term: {max_grades_termU}
Minimum grade(s) and in which term(s): {min_gradesU:.2f} in Term: {min_grades_termU}
Do you have any repeated course(s)? None\n""")
                myFile.write(f"""============================================================
*****************\t Graduate(M) Level\t *****************
============================================================
Overall average (major and minor) for all terms: {ave_gradesM:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1M:.2f}
\t Term 2: {ave_term2M:.2f}
\t Term 3: {ave_term3M:.2f}
Maximum grade(s) and in which terms(s): {max_gradesM:.2f} in Term: {max_grades_termM}
Minimum grade(s) and in which term(s): {min_gradesM:.2f} in Term: {min_grades_termM}
Do you have any repeated course(s)? None\n""")
                myFile.write(f"""
============================================================
******************\t Graduate(D) Level\t ******************
============================================================
Overall average (major and minor) for all terms: {ave_gradesD:.2f}
Average (major and minor) of each term:
\t Term 1: {ave_term1D:.2f}
\t Term 2: {ave_term2D:.2f}
\t Term 3: {ave_term3D:.2f}
\t Term 4: {ave_term4D:.2f}
Maximum grade(s) and in which terms(s): {max_gradesD:.2f} in Term: {max_grades_termD}
Minimum grade(s) and in which term(s): {min_gradesD:.2f} in Term: {min_grades_termD}
Do you have any repeated course(s)? None """)
                
                # Open the txt file.
                os.startfile(filename)
                myFile.close()

                time.sleep(5)
                os.system('cls')
                menuFeature(stdID, student_level, _degree, count)