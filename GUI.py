# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:56:50 2019

@author: rszymczak
"""

import tkinter as tk

root = tk.Tk()
root.title('Historical Database Transcriber')
#root.geometry('400x400')
canvas =tk.Canvas(root, height=520, width=900)
canvas.pack()

# =============================================================================
# background
# =============================================================================
background_image = tk.PhotoImage(
    file='Abstract-Wave-PNG-Photo.png'
    )
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# =============================================================================
# functions
# =============================================================================
#def phrase_generator():
#    phrases = {1:'thank you', 2:'one moment please'}
#    # if number is input return the related phrase
#    user_input = input('idk rn lol: ')
#    return phrases.get(user_input)

#def phrase_displayer():
#    phrase = phrase_generator()
#    phrase_display = tk.Text(master=root, height=10, width=30)
#    phrase_display.grid(column=1, row=5)
#    phrase_display.insert(tk.END, phrase)

def testfunc_in(x):
    x = entry.get()
    label['text'] = testfunc_out(x) 
    
def testfunc_out(x):
    return x*2    

# =============================================================================
# frames
# =============================================================================
frame = tk.Frame(root, bg ='#80c1ff', bd=5)
frame.place(
    relx=0.5, 
    rely=0.1, 
    relwidth=0.75, 
    relheight=0.1, 
    anchor='n'
    )

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(
    relx=0.5, 
    rely=0.25, 
    relwidth=0.75, 
    relheight=0.6, 
    anchor='n'
    )

# =============================================================================
# labels
# =============================================================================
#title = tk.Label(text = 'welcome to HDB transcriber')
#title.pack()
#
label = tk.Label(
    lower_frame
    )
label.place(
    relwidth=1,
    relheight=0.25
    )


# =============================================================================
# entry fields for the user
# =============================================================================
entry = tk.Entry(
    frame, 
    font=40)
entry.place(
    relwidth=0.65, 
    relheight=1,
    )

#comment_field = tk.Text(master=root, height=5, width=30)
#comment_field.pack(side='bottom', fill='x')

# =============================================================================
# buttons
# =============================================================================
button1 = tk.Button(
    frame, 
    text='go', 
    font=40, 
    command=lambda: testfunc_in(entry.get())
    )
#button1.grid(column=0, row=6)
#button1.pack(side='left', fill='both', expand=True)
button1.place(
    relx=0.7,
    relheight=1,
    relwidth=0.25,
    )



root.mainloop()

