from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text

root = Tk()
root.title("MindMate")
root.geometry("675x675")
root.resizable(False, False)
root.config(bg="#900C3F")

def ask():
    ask_val = speech_to_text.speech_to_text()  
    print(f"Captured speech: {ask_val}")  
    bot_val = action.action(ask_val)  
    text.insert(END, "Me --> " + ask_val + "\n")
    if bot_val:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
    if bot_val == "okay sir":
        root.destroy()


def delete():
    text.delete("1.0", END)

def send():
    send_val = entry.get()
    bot_val = action.action(send_val)
    text.insert(END, "Me --> " + send_val + "\n")
    if bot_val:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()


frame = LabelFrame(root, padx=180, pady=7, borderwidth=3, relief="raised", bg="#E9967A")
frame.grid(row=0, column=1, padx=55, pady=10)

text_label = Label(frame, text="My MindMate", font=("arial", 14, "bold"), bg="#CCCCFF")
text_label.grid(row=0, column=0, padx=20, pady=10)


image = ImageTk.PhotoImage(Image.open("image/wa.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)


text = Text(root, font=("arial"), bg="#CD5C5C")
text.place(x=155, y=350, width=375, height=120)

entry = Entry(root, justify=CENTER)
entry.place(x=155, y=490, width=375, height=30)


Button(root, text="ASK", bg="#CCCCFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask).place(x=100, y=540)
Button(root, text="SEND", bg="#CCCCFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send).place(x=300, y=540)
Button(root, text="DELETE", bg="#CCCCFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete).place(x=500, y=540)

root.mainloop()
