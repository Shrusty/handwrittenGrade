import tkinter as tk
from tkinter import filedialog
def create_table_window(sim,avg):
    # Create the Tkinter window
    window = tk.Tk()

    avg=avg*100
    table_frame = tk.Frame(window)
    table_frame.pack(pady=20)
    r1=sim[0]*100 if len(sim)>=1 else 'NA'
    r2=sim[1]*100 if len(sim)>=2 else 'NA'
    r3=sim[2]*100 if len(sim)>=3 else 'NA'
    # Create the table labels
    if avg>=90:
        clas='A+'
    elif avg>=80:
        clas='A'
    elif avg>=70:
        clas='B'
    elif avg>=60:
        clas='C'
    elif avg>=50:
        clas='D'
    elif avg>=40:
        clas='E'
    else:
        clas='F'
    labels = [
        ['Question Number','Percentage'],
        ['Q1', round(r1,2)],
        ['Q2', round(r2,2)],
        ['Q3', round(r3,2)],
        ['Average', round(avg,2)],
        ['Class', clas]
    ]