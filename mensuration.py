from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import pandas as pd
from tkinter import ttk
import webbrowser

def mensus_link():
    shopee_link = "https://pharmeasy.in/blog/10-effective-home-remedies-for-irregular-periods/"
    webbrowser.open(shopee_link)

def mensus():
    window = tk.Tk()
    window.resizable(False, False)
    window.configure(bg='lightpink')
    window.geometry('750x760')
    window.title('You are late :(')

    label = ttk.Label(
        window,
        text=(
            "Menses is the process of discharge of blood from the vagina caused by detachment of the uterine wall (endometrium). "
            "Before detachment, the endometrium undergoes thickening, containing blood vessels. If there is no fertilization of the sperm with the egg, "
            "then this endometrium will shed and come out along with the blood. Mens is a natural monthly cycle in women. The normal cycle of menses generally occurs every 21 to 35 days. "
            "In each period, bleeding during menses occurs 3 to 7 days. However, some women have different cycles and the length of the occurrence of menses. "
            "Some may experience late menses even if they are not pregnant. "
            "Factors include fatigue, stress, contraceptives, PCOS, thyroid disorders, smoking, and menopause. "
            "Do not panic, natural remedies include taking vitamin C, turmeric, ginger tea, relaxation, and warm baths."
        ),
        justify="center",
        wraplength=450
    )
    label.pack(pady=10)

    # Load CSV data
    df = pd.read_csv('duration_of_cycle.csv')

    month = df['month']
    mensus_duration = df['Mensus Duration'].fillna(0).astype(float)
    folicular_duration = df['Follicular Duration'].fillna(0).astype(float)
    ovulation_duration = df['Ovulation Duration'].fillna(0).astype(float)
    luteal_duration = df['Luteal Duration'].fillna(0).astype(float)

    # Create figure
    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)

    # Plot stacked bars
    ax.bar(range(len(month)), mensus_duration, label='Mensus Duration', color='blue')
    ax.bar(range(len(month)), folicular_duration, bottom=mensus_duration, label='Follicular Duration', color='orange')
    ax.bar(range(len(month)), ovulation_duration, bottom=[i+j for i,j in zip(mensus_duration, folicular_duration)],
           label='Ovulation Duration', color='green')
    ax.bar(range(len(month)), luteal_duration,
           bottom=[i+j+k for i,j,k in zip(mensus_duration, folicular_duration, ovulation_duration)],
           label='Luteal Duration', color='purple')

    ax.set_xlabel('Month')
    ax.set_ylabel('Duration (days)')
    ax.set_title('Duration of the Menstrual Cycle Each Month')

    # Fixed tick labels warning
    ax.set_xticks(range(len(month)))
    ax.set_xticklabels(month, rotation=90)
    ax.legend()

    # Embed figure in Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    button = tk.Button(window, text="More details", command=mensus_link)
    button.pack(pady=10)

    window.mainloop()
