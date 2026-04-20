from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt


months_list = []
absences_list = []

def displaying(e):

    month_val = document.getElementById('monthOfTheYear').value
    absence_input = document.getElementById('absences').value

    if not absence_input:
        return
    
    absence_val = int(absence_input)


    months_list.append(month_val)
    absences_list.append(absence_val)

    fig, ax = plt.subplots()
    
    ax.plot(months_list, absences_list, marker='o', linestyle='-', color='teal')
    ax.set_title("Monthly Attendance (Absences)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Absences")
    ax.grid(True)

    output_div = document.getElementById('output')
    output_div.innerHTML = "" 
    display(fig, target="output")