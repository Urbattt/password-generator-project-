from tkinter import* 
import random 

root=Tk()
root.title("Password Generator")
root.geometry("400x400")
label = Label(root)
password = Entry(root)
guessedpassword = Label(root)

array_3d = [[["1","2","3","4","5","6","7","8"], ["Smelly","King","Man"], ["A","B","C","D","E","F","G","H","I"]]]
print(array_3d[0][2][3])



def new_password():
    random_no_1 = random.randint(0,7)
    random_no_2 = random.randint(0,2)
    random_no_3 = random.randint(0,8)
    
    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    label["text"] = "Generated Password : " +  letter1 + "" + letter2 + "" + letter3
    guessed=password.get()
    guessedpassword["text"] = "guessed password : " + str(guessed)
    
btn = Button(root, text = "New Password", command = new_password)
btn.place(relx=0.5, rely=0.6, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor= CENTER)

password.place( relx = 0.5, rely = 0.4, anchor = CENTER)
guessedpassword.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()