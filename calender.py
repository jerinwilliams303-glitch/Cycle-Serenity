import pandas as pd
import calendar
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


def convert_to_calender(data_prediction):
    root = tk.Toplevel()
    root.configure(bg= "lightpink")
    root.title("Menstural Cycle Calender")
    root.geometry("500x500")

    # frame for calender
    frame_calendar = tk.Frame(root)
    frame_calendar.pack(pady=20)

    # navigation for the following moths
    def previous_month():
        nonlocal month, year
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        show_calendar()

    def next_month():
        nonlocal month, year
        month += 1
        if month > 12:
            month = 1
            year += 1
        show_calendar()

    btn_previous = tk.Button(root, text="<<", command=previous_month)
    btn_previous.place(x=20, y=20)
    btn_next = tk.Button(root, text=">>", command=next_month)
    btn_next.place(x=60, y=20)

    #function to display the calender
    def show_calendar():
        # Mdelete existing calender
        for widget in frame_calendar.winfo_children():
            widget.destroy()

        # get the number of days in the selected moth
        num_days = calendar.monthrange(year, month)[1]

        # create month and year titles
        month_label = tk.Label(frame_calendar, text=calendar.month_name[month] + " " + str(year), font=("Arial", 16, "bold"))
        month_label.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

        # make labels untuk nama-nama hari
        days_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for idx, day_label in enumerate(days_labels):
            label = tk.Label(frame_calendar, text=day_label)
            label.grid(row=1, column=idx, padx=5, pady=5)

        #determine the coloumn and row indexes for the first day of the month
        first_day = datetime(year, month, 1)
        col_idx = first_day.weekday()
        row_idx = 2

        # display dates in the calender
        for day in range(1, num_days + 1):
            if col_idx > 6:
                col_idx = 0
                row_idx += 1

            # determines the background colour based on the phase of the menstural cycle
            background_color = "white"
            for _, row in data_prediction.iterrows():
                date_start_mensus = datetime.strptime(row['start date of mensus'], "%d-%m-%Y")
                date_end_mensus = datetime.strptime(row['end date of menses'], "%d-%m-%Y")
                date_start_follicular = datetime.strptime(row['start date of follicular'], "%d-%m-%Y")
                date_end_follicular= datetime.strptime(row['end date of follicular'], "%d-%m-%Y")
                date_start_ovulation = datetime.strptime(row['start date of ovulation'], "%d-%m-%Y")
                date_end_ovulation = datetime.strptime(row['end date of ovulation'], "%d-%m-%Y")
                date_start_luteal = datetime.strptime(row['start date of luteal'], "%d-%m-%Y")
                date_end_luteal = datetime.strptime(row['end date of ovule'], "%d-%m-%Y")

                if date_start_mensus <= datetime(year, month, day) <= date_end_mensus:
                    background_color = "pink"
                    break
                elif date_start_follicular <= datetime(year, month, day) <= date_end_follicular:
                    background_color = "lightblue"
                    break
                elif date_start_ovulation <= datetime(year, month, day) <= date_end_ovulation:
                    background_color = "yellow"
                    break
                elif date_start_luteal <= datetime(year, month, day) <= date_end_luteal:
                    background_color = "lightgreen"
                    break

            # make a label for the date
            label = tk.Label(frame_calendar, text=day, bg=background_color, padx=10, pady=5)
            label.grid(row=row_idx, column=col_idx, padx=5, pady=5)

            col_idx += 1

    frame_text = ttk.Frame(root)
    frame_text.place(x=200, y=350)

    label_text = ttk.Label(frame_text, text='- Pink = Mensturation\n- blue = follicular\n- yellow = Ovulation\n- green = Luteal')
    label_text.pack()

    # initialies the current month and year
    today = datetime.now()
    month = today.month
    year = today.year

    # displays the calender
    show_calendar()

    root.mainloop()

# reading prediction data from csv file using pandas
data_prediction = pd.read_csv("mensus_cycle.csv")

# calls the function to display the calender with data from file CSV

def calender():
   convert_to_calender(data_prediction)

def confirm():
    import mensuration
    result = messagebox.askokcancel('confirmation', 'Have you had your period? If so, press Ok')
    if result == True:
        pass
    else:
        mensuration.mensus()
