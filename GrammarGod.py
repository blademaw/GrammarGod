from tkinter import *
import enchant
import re

# Defining the window:
root = Tk()
root.geometry("700x300")

# variable definitions:
versionNumber = "0.0.1"
root.title("GrammarGod "+versionNumber)
dictionary = enchant.Dict("en_US")

# functions
def readText():
    # clearing
    textCorrections.delete("1.0", END)
    textOUT.delete("1.0", END)

    # getting input
    textToRead = textIN.get("1.0", END)

    # calling spellCheck to verify words
    spellCheck(textToRead)

def spellCheck(text):
    textToOUT = ""
    textCor = "WRONG WORDS DETECTED:\n"
    wordList = text.split()
    for word in wordList:
        if dictionary.check(re.sub(r"[,.;@#?!&$]+\ *", "", word)) is False:
            textCor += (word+" --> did you mean "+", ".join((dictionary.suggest(word)))+"?\n")
            textToOUT += " ___"
        else:
            textToOUT += " "+word
            pass

    textCorrections.insert("1.0", textCor)
    textOUT.insert("1.0", textToOUT)


# Title frame to put the title in the middle of the GUI window
titleFrame = Frame(root, bd=4)
titleFrame.pack(side=TOP)

# Main frame for input and output boxes
mainFrame = Frame(root, bd=4)
mainFrame.pack(side=LEFT)

Label(titleFrame, bd=4, text="Welcome to GrammarGod Version "+versionNumber+".").pack()

Label(mainFrame, bd=2, text="Enter your text below:").pack()
textIN = Text(mainFrame, bd=2, font=("Helvetica",10), height=5, width=50, wrap=WORD)
textIN.pack()

submitButton = Button(mainFrame, padx=4, pady=4, bd=2, text="Fix Text!", justify=RIGHT, command=lambda: readText())
submitButton.pack()

Label(mainFrame, bd=2, text="Corrected text is shown below:").pack()
textOUT = Text(mainFrame, bd=4, font=("Helvetica",10), height=5, width=50, wrap=WORD)
textOUT.pack()
#===================================================>

#Output log frame on the right hand side of the GUI
correctionsFrame = Frame(root, bd=4)
correctionsFrame.pack(side=RIGHT)

Label(correctionsFrame, bd=2, text="Corrections made:").pack()
textCorrections = Text(correctionsFrame, bd=4, font=("Helvetica",10),height=5, width=50, wrap=WORD)
textCorrections.pack()

root.mainloop()
