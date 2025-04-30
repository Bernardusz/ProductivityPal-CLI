from allfunctions import Notes, MathNotes, LanguageNotes, ScienceNotes, ProductivityPal

if __name__ == "__main__":
    StudyPal = ProductivityPal()
    with open("welcome.txt", "r") as f:
        data = f.readlines()
        for line in data:
            print(line)
    
    while True:
        userinput = input("What do you want to do ?: ").lower()

        #Notes related ifs:
        if userinput == "add note": #done
            try:
                title = input("Input the title : ")
                desc = input("Input the description : ")
                subject = input("Input the subject : ")
                print("Keep inputting your notes line by line, type END if you're finished")
                print("---")
                lines = []
                while True:
                    line = input()
                    if line == "END" or line == "":
                        break
                    lines.append(line)
                notes = "\n".join(lines)
                StudyPal.add_notes(title, subject, desc, notes)
                print(notes)
                print("Notes added !")
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error: {e}")
                print("Invalid input !")
                print("------------------------------------------------------")

        elif userinput == "see note": #done
            try:
                title = input("Input the title : ")
                subject = input("Input the subject : ")
                note = StudyPal.see_notes(title, subject)
                try:
                    print(f"Title : {note['Title']} \nSubject : {note['Subject']} \nDesc : {note['Desc']}")
                    print("---")
                    print(f"Note : \n{note['Note']}")
                    print("---")
                except:
                    print(note)
                try:
                    print("Vocab or Formula :")
                    print(StudyPal.see_vocab_formula(title))
                except:
                    pass
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error: {e}")
                print("------------------------------------------------------")

        elif userinput == "edit note": #done
            try:
                title = input("Input the title : ")
                subject = input("Input the subject")
                StudyPal.edit_notes(title, subject)
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error: {e}")
                print("------------------------------------------------------")
        
        elif userinput == "add formula": #done
            try:
                title = input("Input the title : ")
                name = input("Input the name of formula : ")
                formula = input("Input the formula : ")
                StudyPal.add_formula(name, formula, title)
            except Exception as e:
                print(f"Error: {e}")
            print("------------------------------------------------------")

        elif userinput == "add vocab": #done
            try:
                title = input("Input the title : ")
                word = input("Input the word : ")
                meaning = input("Input the meaning : ")
                StudyPal.add_vocab(word, meaning, title)
            except Exception as e:
                print(f"Error: {e}")
            print("------------------------------------------------------")

        elif userinput == "see vocab/formula": #done
            try:
                title = input("Input the title : ")
                data = StudyPal.see_vocab_formula(title)
                print(data)
            except Exception as e:
                print(f"Error: {e}")
            print("------------------------------------------------------")

        elif userinput == "remove note": #done
            try:
                title = input("Input the title : ")
                subject = input("Input the subject : ")
                StudyPal.remove_notes(title, subject)
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error: {e}")
                print("------------------------------------------------------")

        elif userinput == "export note to txt": #done
            try:
                title = input("Input the title : ")
                subject = input("Input the subject : ")
                file = input("Enter your file name : ")
                StudyPal.export_txt(file, title, subject)
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error: {e}")
                print("------------------------------------------------------")

        #Tasks related ifs
        elif userinput == "add task": #done
            try:
                title = input("Input the title : ")
                desc = input("Input the description : ")
                priority = input("Input the priority [Low/Medium/High] : ")
                deadline = input("Input the deadline [Day/Month/Year] : ")
                StudyPal.add_task(title, desc, priority, deadline)
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error: {e}")
                print("------------------------------------------------------")

        elif userinput == "see all tasks": #done
            try:
                data = StudyPal.see_task
                for task in data:
                    print(f"Title : {data[task]['Title']} \nDescription : {data[task]['Description']} \nPriority : {data[task]['Priority']} \nDeadline : {data[task]['Deadline']} \nFinished : {data[task]['Finished']}")
                    print("---")
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error: {e}")
                print("------------------------------------------------------")

        elif userinput == "see task by": #done
            try:
                by = input("Sort by [Priority/Incomplete-Finished/Close to deadline]: ")
                if by == "Priority":
                    type = input("Input the priority [Low/Medium/High]: ")
                    data = StudyPal.see_task_by(by, type)
                    for task in data:
                        print(f"Title : {data[task]['Title']} \nDescription : {data[task]['Description']} \nPriority : {data[task]['Priority']} \nDeadline : {data[task]['Deadline']} \nFinished : {data[task]['Finished']}")
                        print("---")

                elif by == "Incomplete-Finished":
                    type = input("Input Finished or Unfinished : ")

                    if type == "Finished":
                        data = StudyPal.see_task_by(by, True)
                        for task in data:
                            print(f"Title : {data[task]['Title']} \nDescription : {data[task]['Description']} \nPriority : {data[task]['Priority']} \nDeadline : {data[task]['Deadline']} \nFinished : {data[task]['Finished']}")
                            print("---")

                    elif type == "Unfinished":
                        data = StudyPal.see_task_by(by, False)
                        for task in data:
                            print(f"Title : {data[task]['Title']} \nDescription : {data[task]['Description']} \nPriority : {data[task]['Priority']} \nDeadline : {data[task]['Deadline']} \nFinished : {data[task]['Finished']}")
                            print("---")
                    else:
                        print("Invalid input !")

                else:
                    print("Invalid input !")
            except Exception as e:
                print(f"Error: {e}")
            print("------------------------------------------------------")

        elif userinput == "mark done": #done
            title = input("Input the title : ")
            result = StudyPal.mark_done(title)
            print({result})
    
        #json related ifs
        elif userinput == "save to json":
            try:
                file = input("Input the file's name [text.json] : ")
                StudyPal.save_json(file)
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error: {e}")
                print("------------------------------------------------------")
        
        elif userinput == "load from json":
            try:
                file = input("Input the file's name [text.json] : ")
                StudyPal.load_json(file)
            except Exception as e:
                print(f"Error: {e}")
            print("------------------------------------------------------")
        
        #pomodoro related ifs
        elif userinput == "study": #done
            try:
                print("Good ! Let's get started !\nChoose a note !")

                title = input("Input the title : ")
                subject = input("Input the subject : ")
                data = StudyPal.see_notes(title, subject)

                print(f"Title : {data['Title']} \nSubject : {data['Subject']} \nDesc : {data['Desc']}")
                print(data["Note"])


                pomodoro = input("Choose ! 25/5 or 50/10 !: ")
                StudyPal.pomodoro(pomodoro, title, subject)
            except Exception as e:
                print(f"Error: {e}")
            print("------------------------------------------------------")

        elif userinput == "exit": #done
            print("Don't forget to study ! More studies = Brighter future !")
            break

        else: #done
            print("Invalid command !")
            print("------------------------------------------------------")








        



                 
                