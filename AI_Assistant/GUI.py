from tkinter import* 
from PIL import Image, ImageTk
root = Tk()
import speech_text
import execute


root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

#Ask function 
def ask():
    user_val = speech_text.speech_to_txt()
    bot_val = execute.execute(user_val)
    text.insert(END, "user--->"+ user_val + "\n")
    if bot_val != None:
        text.insert(END, "BOT <---"+str(bot_val)+ "\n")
        
    if bot_val == "this want I found":
        root.destroy()
    
#Delete function
def delete():
    print("Delete command")

#Send function
def send():
    print("Send command")
    

#frame 
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)

#text label 
text_label = Label(frame, text="AI Assistant", font=("comic Sans ms", 14 , "bold"), bg="#356696")
text_label.grid(row=0,column=0,padx=20,pady=10)

#Image 
image  = ImageTk.PhotoImage(Image.open("Images/image.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

#Text widget 
text = Text(root, font=('courier 10 bold'), bg="#356696")
text.grid(row=2, column=0)
text.place(x=100, y=375, width=375, height=100)

#Entry Widget 
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

#Button1 
Button1 = Button(root, text="ASK", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

#Button2
Button2 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete)
Button2.place(x=400, y=575)

#Button3
Button3 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button3.place(x=225, y=575)

root.mainloop()

