import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
#----------quiz--------------

root = tk.Tk()
root.geometry('600x600')

questions = ["Who developed python programming language?","which keyword is used for function in python?","which of the following is correct extension of python file?",
             "what does pip stand for?","what is maximum possible length of an identifier in python?"]
options = [['A. Wick van Rossum','B.  Rasmus Lerdorf','C. Guido van Rossum','D. Niene stom','C. Guido van Rossum'],['A.Function','B.def','C. Fun','D. Define','B.def'],
           ['A. .python','B. .py','C. .pythonfile','D. .pyfile','B. .py'],['A.Pip Install Python','B.Pip Install Packages','C. Preferred Installer Program ','D.None of the above','C. Preferred Installer Programe'],
           ['A. 79 character','B. 31 character','C.  63 character','D. None of the above','D. None of the above']]


frame = tk.Frame(root, padx=10, pady=10,bg='navy')
question_label = tk.Label(frame,height=5, width=28,bg='lightblue',fg="black", 
                          font=('Arial', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="navy", variable=v1, font=('Arial', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="navy", variable=v2, font=('Arial', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="navy", variable=v3, font=('Arial', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="navy", variable=v4, font=('Arial', 20), 
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='red', font=('Arial', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)


index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'





    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check your Results here'





displayNextQuestion()

root.mainloop()