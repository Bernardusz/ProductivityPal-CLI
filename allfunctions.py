import datetime
import time
import json

x = datetime.datetime.now()
today = x.strftime("%x").split("/")

month = int(today[0])
date = int(today[1])
year = int(today[2])

class Notes:
    def __init__(self, title, subject, desc, note):
        self.title = title
        self.desc = desc
        self.subject = subject
        self._note = note

    def change_notes(self, new_note):
        self._note = new_note

    @property
    def return_note(self):
        return self._note

class ScienceNotes(Notes):
    def __init__(self, title, subject, desc, note):
        super().__init__(title, subject, desc, note)
        self.formulas = {}

    def add_formulas(self, name, formula):
        self.formulas[name] = formula
    
    def change_notes(self, new_note):
        super().change_notes(new_note)

    @property
    def return_note(self):
        return self._note

    @property
    def return_formula(self):
        return self.formulas

class MathNotes(Notes):
    def __init__(self, title, subject, desc, note):
        super().__init__(title, subject, desc, note)
        self.formulas = {}


    def add_formulas(self, name, formula):
        self.formulas[name] = formula

    def change_notes(self, new_note):
        super().change_notes(new_note)

    @property
    def return_note(self):
        return self._note

    @property
    def return_formula(self):
        return self.formulas

class LanguageNotes(Notes):
    def __init__(self, title, subject, desc, note):
        super().__init__(title, subject, desc, note)        
        self.vocab = {}

    def add_vocab(self, word, translation):
        self.vocab[word] = translation

    def change_notes(self, new_note):
        super().change_notes(new_note)

    @property
    def return_note(self):
        return self._note
    
    @property
    def return_vocab(self):
        return self.vocab

class Tasks:
    def __init__(self, name, desc, priority, day, month, year):
        self.title = name
        self.desc = desc
        self.priority = priority
        self.deadline = [day, month, year]
        self.finished = False

    def marked_done(self):
        self.finished = True

class ProductivityPal:
    def __init__(self):
        self.notes = {}
        self.tasks = {}
        self.languages = ["English", "Indonesian", "Hungarian", "Polish", "Chinese", "French", "Italian", "Spanish", "German", "Russian"] 
        self.available = ["Science", "Math", "Languages"]
        self.logs = {}

        self.logs["25/5"] = {}
        self.logs["50/10"] = {}

    #Notes related methods
    def add_notes(self, title, subject, desc, note):
        if subject == "Science":
            self.notes[title] = ScienceNotes(title, "Science", desc, note)
        elif subject == "Math":
            self.notes[title] = MathNotes(title, "Math", desc, note)
        elif subject in self.languages:
            language = self.languages.index(subject)
            self.notes[title] = LanguageNotes(title, self.languages[language],desc, note)
        else:
            self.notes[title] = Notes(title, subject, desc, note)

    def see(self, title, wanted_subject):
        if title in self.notes:
            if self.notes[title].subject == wanted_subject:
                return {"Title" : self.notes[title].title,
                        "Subject" : self.notes[title].subject,
                        "Desc" : self.notes[title].desc,
                        "Note" : self.notes[title].return_note}
            else:
                return f"{title} with {wanted_subject} subject isn't found !"
        else:
            return f"{title} doesn't exist !"

    def see_notes(self, title, subject):
        if subject == "Science":
            return self.see(title, "Science")
        elif subject == "Math":
            return self.see(title, "Math")
        elif subject in self.languages:
            language = self.languages.index(subject)
            return self.see(title, self.languages[language])
        else:
            return self.see(title, subject)
    
    def edit_notes(self, title, subject):
        if title in self.notes:
            if self.notes[title].subject == subject:
                userinput = input("What do you want to edit ? : ").lower()
                if userinput in ["title", "judul"]:
                    newtitle = input("Enter the new title : ")
                    self.notes[newtitle] = self.notes.pop(title)
                    self.notes[newtitle].title = newtitle
                    
                    del self.notes[title]
                    print("Succsesfully edited !")
                elif userinput in ["notes", "isi", "note"]:
                    print("Enter the new note : ")
                    lines = []
                    while True:
                        line = input()
                        if line == "END" or line == "":
                            break
                        lines.append(line)
                    notes = "\n".join(lines)
                    self.notes[title].change_notes(notes)
                    print("Succsesfully edited !")
                elif userinput in ["desc", "description"]:
                    newdesc = input("Enter the new desc : ")
                    self.notes[title].desc = newdesc
                    print("Succsesfully edited !")
                else:
                    print("Invalid command !")
            else:
                print(f"{title} with {subject} subject isn't found !")
        else:
            print(f"{title} doesn't exist !")

    def add_formula(self, name, formula, title):
        if title in self.notes:
            if self.notes[title].subject == "Math" or self.notes[title].subject == "Science":
                self.notes[title].add_formulas(name, formula)
                print("Sucsessfully added !")
            else:
                print(f"The subject doesn't match !")
        else:
            print("Note isn't find !")

    def add_vocab(self, word, meaning, title):
        if title in self.notes:
            if self.notes[title].subject in self.languages:
                self.notes[title].add_vocab(word, meaning)
                print("Sucsessfully added !")
            else:
                print(f"The subject doesn't match !")
        else:
            print("Note isn't find !")

    def see_vocab_formula(self, title):
        if title in self.notes:
            if self.notes[title].subject == "Math" or self.notes[title].subject == "Science":
                return self.notes[title].return_formula
            elif self.notes[title].subject in self.languages:
                return self.notes[title].return_vocab
            else:
                return f"Unable to get !"
        else:
            return f"{title} doesn't exist !"
        
    def remove_notes(self, title, subject):
        if title in self.notes:
            if self.notes[title].subject == subject:
                del self.notes[title]
                print("Sucsessfully removed !")
            else:
                print(f"{title} with {subject} subject isn't found !")
        else:
            print(f"{title} doesn't exist !")

    def export_txt(self, file, title, subject):
        notes = self.see_notes(title, subject)
        if isinstance(notes, dict):
            with open(file, "a") as f:
                f.write(f"Title : {notes['Title']} \nSubject : {notes['Subject']} \nDescription : {notes['Desc']} \nNote : \n---\n{notes['Note']}\n---")
                f.write(f"\n{self.see_vocab_formula(notes['Title'])}")
        else:
            print("Error !")
    #Tasks related methods
    def add_task(self, title, desc, priority, deadline):
        day, month, year = deadline.split("/")
        self.tasks[title] = Tasks(title, desc, priority, int(day), int(month), int(year))

    @property
    def see_task(self): 
        placeholder = {}
        for task in self.tasks:
            title = self.tasks[task].title
            desc = self.tasks[task].desc
            priority = self.tasks[task].priority
            deadline = self.tasks[task].deadline
            finished = self.tasks[task].finished
            
            placeholder[title] = {"Title" : title,
                                  "Description" : desc,
                                  "Priority" : priority,
                                  "Deadline" : deadline,
                                  "Finished" : finished}
        return placeholder
            
    def see_task_by(self, by, type): #Decode the placeholder first !
        if by == "Priority":
            placeholder = {}
            for task in self.tasks:
                if self.tasks[task].priority == type:

                    title = self.tasks[task].title
                    desc = self.tasks[task].desc
                    priority = self.tasks[task].priority
                    deadline = self.tasks[task].deadline
                    finished = self.tasks[task].finished

                    placeholder[title] = {"Title" : title,
                                  "Description" : desc,
                                  "Priority" : priority,
                                  "Deadline" : deadline,
                                  "Finished" : finished}
            return placeholder
                
        elif by == "Incomplete-Finished":
            placeholder = {}
            for task in self.tasks:
                if self.tasks[task].finished == type: #Type will be True or False
                    title = self.tasks[task].title
                    desc = self.tasks[task].desc
                    priority = self.tasks[task].priority
                    deadline = self.tasks[task].deadline
                    finished = self.tasks[task].finished

                    placeholder[title] = {"Title" : title,
                                  "Description" : desc,
                                  "Priority" : priority,
                                  "Deadline" : deadline,
                                  "Finished" : finished}

            return placeholder

    def mark_done(self, title):
        if title in self.tasks:
            self.tasks[title].marked_done()
            return f"Done !"
        else:
            return f"Unable to find task !"
        
    #json related methods
    def save_json(self, file):
        with open(file, "w") as f:
            data = {}
            data["Notes"] = {}
            data["Tasks"] = {}
            data["Logs"] = {}
        # Notes first
            for note in self.notes:
                instance_note = self.notes[note]
                title = instance_note.title
                subject = instance_note.subject
                desc = instance_note.desc
                notes = instance_note.return_note

                if subject not in data["Notes"]:
                    data["Notes"][subject] = {}

                data["Notes"][subject][title] = {"Title" : title,
                                                 "Subject" : subject,
                                                 "Description" : desc,
                                                 "Note" : notes}
        # Task
            for task in self.tasks:
                instance_task = self.tasks[task]
                title_task = instance_task.title
                desc_task = instance_task.desc
                priority = instance_task.priority
                deadline = instance_task.deadline
                finished = instance_task.finished

                if "Unfinished" not in data["Tasks"]:
                    data["Tasks"]["Unfinished"] = {}
                if "Finished" not in data["Tasks"]:
                    data["Tasks"]["Finished"] = {}

                if finished == False:
                    data["Tasks"]["Unfinished"][title_task] = {"Title" : title_task,
                                                              "Description" : desc_task,
                                                              "Priority" : priority,
                                                              "Deadline" : deadline,
                                                              "Finished" : finished}
                elif finished == True:
                    data["Tasks"]["Finished"][title_task] = {"Title" : title_task,
                                                            "Description" : desc_task,
                                                            "Priority" : priority,
                                                            "Deadline" : deadline,
                                                            "Finished" : finished}
        
        #Logs
            for log1 in self.logs["25/5"]:
                if "25/5" not in data["Logs"]:
                    data["Logs"]["25/5"] = {}
                data["Logs"]["25/5"][log1] = self.logs["25/5"][log1]

            for log2 in self.logs["50/10"]:
                if "50/10" not in data["Logs"]:
                    data["Logs"]["50/10"] = {}
                data["Logs"]["50/10"][log2] = self.logs["50/10"][log2]

            json.dump(data, f, indent=4)

    def load_json(self, file):
        with open(file, "r") as f:
            data = json.load(f)
            #Note first
            try:
                for subject in data["Notes"]:
                    for note in data["Notes"][subject]:
                        title = data["Notes"][subject][note]["Title"]
                        Subject = data["Notes"][subject][note]["Subject"]
                        Desc = data["Notes"][subject][note]["Description"]
                        Note = data["Notes"][subject][note]["Note"]
                        self.add_notes(title, Subject, Desc, Note)
            except:
                pass

            #Task
            try:
                for unfinished_task in data["Tasks"]["Unfinished"]:
                    title_unfinished = data["Tasks"]["Unfinished"][unfinished_task]["Title"]
                    desc_untask = data["Tasks"]["Unfinished"][unfinished_task]["Description"]
                    unpriority = data["Tasks"]["Unfinished"][unfinished_task]["Priority"]
                    undeadline = data["Tasks"]["Unfinished"][unfinished_task]["Deadline"]
                    unfdead = f"{undeadline[0]}/{undeadline[1]}/{undeadline[2]}"
                    self.add_task(title_unfinished, desc_untask, unpriority, unfdead)
            except:
                pass

            try:
                for finished_task in data["Tasks"]["Finished"]:
                    title_finished = data["Tasks"]["Finished"][finished_task]["Title"]
                    findesc_task = data["Tasks"]["Finished"][finished_task]["Description"]
                    finpriority = data["Tasks"]["Finished"][finished_task]["Priority"]
                    findeadline = data["Tasks"]["Finished"][finished_task]["Deadline"]
                    finidead = f"{findeadline[0]}/{findeadline[1]}/{findeadline[2]}"
                    self.add_task(title_finished, findesc_task, finpriority, finidead)
                    self.tasks[title_finished].marked_done()
            except:
                pass

            try:
                for logs25 in data["Logs"]["25/5"]:
                    self.logs["25/5"][logs25] = data["Logs"]["25/5"][logs25]
            except:
                pass
            
            try:
                for logs50 in data["Logs"]["50/10"]:
                    self.logs["50/10"][logs50] = data["Logs"]["50/10"][logs50]
            except:
                pass
    #Pomodoro/Study related methods
    def pomodoro(self, method, title, subject):
        if method == "25/5":
            available_time = 8 #60*25
            time.sleep(available_time/2)
            print("Half the time has passed !")
            time.sleep(available_time/4)
            print("3/4th of the time has passed !")
            time.sleep(0.75)
            print("5 Minutes remaining !")
            time.sleep(60*0.05)
            print("Time's up ! Great job soilder !")
            print("Now go ! Recharge you deserve that 5 minutes break !")
            self.logs["25/5"][title] = {"Title" : title,
                                        "Subject" : subject,
                                        "Pomodoro" : "25/5",
                                        "Date" : today}

        elif method == "50/10":
            available_time = 6.0*0.5
            time.sleep(available_time/2)
            print("Half the time has passed !")
            time.sleep(available_time/4)
            print("3/4th of the time has passed !")
            time.sleep(0.450)
            print("5 Minutes remaining !")
            time.sleep(0.6*5)
            print("Time's up ! Great job soilder !")
            print("Now go ! Recharge you deserve that 10 minutes break !")
            self.logs["50/10"][title] = {"Title" : title,
                                        "Subject" : subject,
                                        "Pomodoro" : "50/10",
                                        "Date" : today}
        else:
            print(f"Invalid method !")