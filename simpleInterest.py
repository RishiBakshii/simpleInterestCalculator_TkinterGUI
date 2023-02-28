from tkinter import *

# declaring constants
PRIMARY_FONT="regular 14"
PRIMARY_BACKGROUND="#141414"
PRIMARY_FONT_COLOR="lightblue"

def calculate_interest():
    try:
        p=int(principal_input.get())
        r=int(roi_input.get())
        t=int(time_input.get())
        si=(p*r*t)/100
        output_label.config(text=f'Simple Interest : {round(si,4)}')
    except Exception as c:
        output_label.config(text="Invalid INPUT!")


# MAIN WINDOW STARTS HERE-->>
root=Tk()
width=400
height=400
root.geometry(f"{width}x{height}")
root.title("Simple Interest")
root.maxsize(width=width,height=height)
root.minsize(width=width,height=height)
root.iconbitmap("calculator_23810.ico")
root.configure(background=PRIMARY_BACKGROUND)

heading=Label(root,text="Calculate Simple Interest",font="regular 17",bg=PRIMARY_BACKGROUND,fg=PRIMARY_FONT_COLOR)
heading.place(x=120,y=50)

principal_label=Label(root,text="Principal",font=PRIMARY_FONT,height=1,background=PRIMARY_BACKGROUND,fg=PRIMARY_FONT_COLOR)
principal_label.place(x=50,y=100)

principal_input=Entry(root,font=PRIMARY_FONT)
principal_input.place(x=140,y=100)

roi_label=Label(root,text="ROI",font=PRIMARY_FONT,height=1,background=PRIMARY_BACKGROUND,fg=PRIMARY_FONT_COLOR)
roi_label.place(x=50,y=140)

roi_input=Entry(root,font=PRIMARY_FONT)
roi_input.place(x=140,y=140)

time_label=Label(root,text="Time",font=PRIMARY_FONT,height=1,background=PRIMARY_BACKGROUND,fg=PRIMARY_FONT_COLOR)
time_label.place(x=50,y=180)

time_input=Entry(root,font=PRIMARY_FONT)
time_input.place(x=140,y=180)

calculate_btn=Button(root,text="Calculate",font=PRIMARY_FONT,bg=PRIMARY_BACKGROUND,fg=PRIMARY_FONT_COLOR,command=calculate_interest)
calculate_btn.place(x=180,y=230)

output_label=Label(root,text="Click On the CALCULATE BUTTON",font="regular 10",bg=PRIMARY_BACKGROUND,fg=PRIMARY_FONT_COLOR)
output_label.place(x=0,y=380)



root.mainloop()