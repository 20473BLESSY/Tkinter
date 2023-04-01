import tkinter as tk
import numpy as np
import pickle
from joblib import dump, load
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
def credit_score():
    try:
        Annual_Income = float(e0.get())
        Monthly_Inhand_Salary = float(e1.get())
        Num_Bank_Accounts = float(e2.get())
        Num_Credit_Card = float(e3.get())
        Interest_Rate = float(e4.get())
        Num_of_Loan = float(e5.get())
        Delay_from_due_date = float(e6.get())
        Num_of_Delayed_Payment = float(e7.get())
        Credit_Mix = float(e8.get())
        Outstanding_Debt = float(e9.get())
        Credit_History_Age = float(e10.get())
        Monthly_Balance = float(e11.get())
    except ValueError:
        messagebox.showerror("Input Error","Invalid input values.Please enter valid integer values.")
        return
    
    model = load('model.joblib')
    userInput = [[Annual_Income,Monthly_Inhand_Salary, 
                   Num_Bank_Accounts, Num_Credit_Card, 
                   Interest_Rate, Num_of_Loan,Delay_from_due_date, Num_of_Delayed_Payment, 
                   Credit_Mix, Outstanding_Debt, 
                   Credit_History_Age, Monthly_Balance]]
    features = np.array(userInput, dtype=int)
    prediction = model.predict(features)
    #result_label.config(text=str(prediction))
    if prediction[0] == "Good":
        #result = "Your Credit Score is Good."
        result_label.config(text="Your Credit Score is Good.",foreground ="green",font=("Helvetica",20))
        img = ImageTk.PhotoImage(Image.open(r"D:\WISE_ML_Project\good2.jpg"))
    elif prediction[0] == "Standard":
        #result = "Your Credit Score is Standard."
        result_label.config(text="Your Credit Score is Standard.",foreground ="Orange",font=("Helvetica",20))
        img = ImageTk.PhotoImage(Image.open(r"D:\WISE_ML_Project\standard2.jpg"))
    else:
        #result = "Your Credit Score is Poor."
        result_label.config(text="Your Credit Score is Poor.",foreground ="red",font=("Helvetica",20))
        img = ImageTk.PhotoImage(Image.open(r"D:\WISE_ML_Project\poor2.jpg"))


    
m = tk.Tk()
m.title("Credit Score Classification")
m.geometry('420x530')
back = Image.open("b_g.jpeg")
back_photo = ImageTk.PhotoImage(back)
back_label = tk.Label(m,image=back_photo)
back_label.place(x=0,y=0,relwidth=1, relheight=1)
button = tk.Button(m,text="KNOW YOUR CREDIT SCORE")
button.grid(row=20,column=5,pady=70,padx=70)
#m.iconbitmap('creditlogo.ico')
def clear_fields():
    e0.delete(0, 'end')
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    e7.delete(0, 'end')
    e8.delete(0, 'end')
    e9.delete(0, 'end')
    e10.delete(0, 'end')
    e11.delete(0, 'end')
tk.Label(m, text="Annual_Income").grid(row=23,column = 5,pady=7,padx=80,ipadx=30)
e0 = tk.Entry(m)
e0.grid(row=23, column=6,pady=7,padx=40)

tk.Label(m, text="Monthly_Inhand_Salary").grid(row=25,column = 5,pady=7,ipadx=12,padx=80)
e1 = tk.Entry(m)
e1.grid(row=25, column=6,pady=7,padx =40)

tk.Label(m, text="Num_Bank_Accounts").grid(row=27,column =5,pady=7,ipadx=16)
e2 = tk.Entry(m)
e2.grid(row=27, column=6,pady=7)

tk.Label(m, text="Num_Credit_Card").grid(row=29,column =5,pady=7,ipadx=25)
e3 = tk.Entry(m)
e3.grid(row=29, column=6,pady=7)

tk.Label(m, text="Interest_Rate").grid(row=31,column = 5,pady=7,ipadx=40)
e4 = tk.Entry(m)
e4.grid(row=31, column=6,pady=7)

tk.Label(m, text="Num_of_Loan").grid(row=33,column =5,pady=7,ipadx=37)
e5 = tk.Entry(m)
e5.grid(row=33, column=6,pady=7)

tk.Label(m, text="Delay_from_due_date").grid(row=35,column=5,pady=7,ipadx=20)
e6 = tk.Entry(m)
e6.grid(row=35, column=6,pady=7)

tk.Label(m, text="Num_of_Delayed_Payment").grid(row=37,column=5,pady=7,ipadx=4)
e7 = tk.Entry(m)
e7.grid(row=37, column=6,pady=7)

tk.Label(m, text="Credit_Mix").grid(row=39,column=5,pady=7,ipadx=47)
e8 = tk.Entry(m)
e8.grid(row=39, column=6,pady=7)

tk.Label(m, text="Outstanding_Debt").grid(row=41,column =5,pady=7,ipadx=28)
e9 = tk.Entry(m)
e9.grid(row=41, column=6,pady=7)

tk.Label(m, text="Credit_History_Age").grid(row=43,column=5,pady=7,ipadx=25)
e10 = tk.Entry(m)
e10.grid(row=43, column=6,pady=7)

tk.Label(m, text="Monthly_Balance").grid(row=45,column=5,pady=7,ipadx=28)
e11 = tk.Entry(m)
e11.grid(row=45, column=6,pady=7)

result_label = tk.Label(m, text="")
result_label.grid(row=56, column=6, columnspan=2,ipady=8,ipadx=50,pady=30)

#result_label = tk.Label(m, text="")
#result_label.grid(row=9, column=0, columnspan=2)

predict_button = tk.Button(m, text="Predict", command=credit_score)
predict_button.grid(row=56, column=5,pady=30,padx=8)
button = tk.Button(m,text="CLEAR",command=clear_fields)
button.grid(row=58,column=6,pady=10)


m.mainloop()