# B and B0 options for Details feature
# Checks if the user inputted B0 it will print the details of both Masteral and Doctoral
                    elif _degree == 'B0':
                        if 'M1' in row:
                            name = row[2]
                            std_id = row[1]
                            level = row[5]
                            degree = row[6]
                            n_terms = row[9]
                            college = row[3]
                            dept = row[4]
                            format = (f"Name: {name}\nStudent ID: {std_id}\nLevel(s): {level}\nDegree: {degree}\nNumber of Terms: {n_terms}\nCollege(s): {college}\nDepartment(s): {dept}\n")
                            print(format)

                            filename = 'std' + stdID + 'details.txt'
                            myFile = open(filename, 'w')
                            filetext = format

                            myFile.write(filetext)
                            os.startfile(filename)
                            myFile.close()

                            time.sleep(5)
                            # os.system('cls')

                        elif 'D1' in row:
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
                        
                # Checks if the user inputted B (Undergraduate and choose from Masteral, Doctoral and Both(B0)) and print the details
                elif student_level == "B":
                    if 'U' in row:
                        name = row[2]
                        std_id = row[1]
                        level = row[5]
                        degree = row[6]
                        n_terms = row[9]
                        college = row[3]
                        dept = row[4]
                        format = (f"Name: {name}\nStudent ID: {std_id}\nLevel(s): {level}\nDegree: {degree}\nNumber of Terms: {n_terms}\nCollege(s): {college}\nDepartment(s): {dept}\n")
                        print(format)

                        filename = 'std' + stdID + 'details.txt'
                        myFile = open(filename, 'w')
                        filetext = format

                        myFile.write(filetext)
                        os.startfile(filename)
                        myFile.close()

                        time.sleep(5)
                        # os.system('cls')   

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
                            format = (f"Name: {name}\nStudent ID: {std_id}\nLevel(s): {level}\nDegree: {degree}\nNumber of Terms: {n_terms}\nCollege(s): {college}\nDepartment(s): {dept}\n")
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
                    
                    # Checks if the user inputted B0 it will print the details of both Masteral and Doctoral
                    elif _degree == 'B0':
                        if 'U' in row:
                            name = row[2]
                            std_id = row[1]
                            level = row[5]
                            degree = row[6]
                            n_terms = row[9]
                            college = row[3]
                            dept = row[4]
                            format = (f"Name: {name}\nStudent ID: {std_id}\nLevel(s): {level}\nDegree: {degree}\nNumber of Terms: {n_terms}\nCollege(s): {college}\nDepartment(s): {dept}\n")
                            print(format)

                            filename = 'std' + stdID + 'details.txt'
                            myFile = open(filename, 'w')
                            filetext = format

                            myFile.write(filetext)
                            os.startfile(filename)
                            myFile.close()

                            time.sleep(5)
                            # os.system('cls')   

                        if 'M1' in row:
                            name = row[2]
                            std_id = row[1]
                            level = row[5]
                            degree = row[6]
                            n_terms = row[9]
                            college = row[3]
                            dept = row[4]
                            format = (f"Name: {name}\nStudent ID: {std_id}\nLevel(s): {level}\nDegree: {degree}\nNumber of Terms: {n_terms}\nCollege(s): {college}\nDepartment(s): {dept}\n")
                            print(format)

                            filename = 'std' + stdID + 'details.txt'
                            myFile = open(filename, 'w')
                            filetext = format

                            myFile.write(filetext)
                            os.startfile(filename)
                            myFile.close()

                            time.sleep(5)
                            # os.system('cls')

                        elif 'D1' in row:
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