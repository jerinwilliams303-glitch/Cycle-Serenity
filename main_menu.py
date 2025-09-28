import csv
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json
import insight
import webbrowser

def main_program():
    while True:
        try:
            file_path = "login_count.json"

            def load_data():
                try:
                    with open(file_path, "r") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    data = {}
                return data

            def save_data(data):
                with open(file_path, "w") as file:
                    json.dump(data, file)

            data = load_data()

            if "login_count" in data:
                login_count = data["login_count"]
            else:
                login_count = 0
                
            login_count += 1

            data["login_count"] = login_count
            save_data(data)

            main_window = tk.Tk()
            main_window.configure(bg='lightpink')
            main_window.geometry('750x750')
            main_window.resizable(False, False)
            main_window.title('Cycle Serenity')

            image = Image.open("foto_tubes.jpg")
            resize_image = image.resize((600,400))
            photo = ImageTk.PhotoImage(resize_image)
            photo_label = tk.Label(main_window, image=photo)
            photo_label.pack(pady=20)

            result1 = tk.StringVar()
            result2 = tk.StringVar()
            result3 = tk.StringVar()
            result4 = tk.StringVar()

            def inputinput():
                if login_count == 1:
                    input_frame = ttk.Frame(main_window)
                    input_frame.pack(fill='x', padx=70, expand=True)

                    label_date_of_last_mensus = ttk.Label(input_frame, text='Date of Your Last Menstruation: (DD-MM-YYYY)')
                    label_date_of_last_mensus.pack(padx=10, pady=10, fill='x', expand=True)
                    entry_date_of_last_mensus = ttk.Entry(input_frame, textvariable=result1)
                    entry_date_of_last_mensus.pack(padx=10, pady=10, fill='x', expand=True)

                    label_average  = ttk.Label(input_frame, text='Average Duration of Your Menses (Days):')
                    label_average.pack(padx=10, pady=10, fill='x', expand=True)
                    entry_average = ttk.Entry(input_frame, textvariable=result2)
                    entry_average.pack(padx=10, pady=10, fill='x', expand=True)

                    def save_data():
                        date = result1.get()
                        average = result2.get()
                        file_name = 'data_input.csv'
                        save_to_csv(date,average,file_name)

                    def check1():
                        try:
                            if result.get().isalpha():
                                raise ValueError('Enter according to format!!')
                        except ValueError:
                            messagebox.showerror('Error')
                            inputinput()

                    def check2():
                        try:
                            if int(result2.get()) == result2.get():
                                raise ValueError('Enter Numbers Only!!')
                        except ValueError:
                            messagebox.showerror('Error')
                            inputinput()

                    def count_mensus():
                        save_data()
                        from INPUT_and_EDIT_PERIOD import mensus
                        mensus()

                    button_next = ttk.Button(input_frame, text='count', command=lambda: (count_mensus(), check1(), check2()))
                    button_next.pack()

            inputinput()

            def save_to_csv(date, average, file_name):
                header = ['Date', 'Average']
                data = [[date, average]]

                with open(file_name, 'w', newline='') as file_mensusdata:
                    writer = csv.writer(file_mensusdata)
                    writer.writerow(header)
                    writer.writerows(data)
      
            def next_page():
                main_window.withdraw()
                def closedwindow1():
                    next_window.withdraw()
                    main_window.deiconify()

                def insightmodule():
                    global insight_window
                    next_window.withdraw()
                    insight_window = tk.Tk()
                    insight_window.configure(bg='lightpink')
                    insight_window.geometry('750x700')
                    insight_window.resizable(False, False)
                    insight_window.title('Insight')

                    def closedwindow2():
                        insight_window.withdraw()
                        next_window.deiconify()

                    button_frame = ttk.Frame(insight_window)
                    button_frame.pack(padx=60, pady=10, fill='x', expand=True)
                    
                    def sportsmodule():
                        
                        insight_window.withdraw()  # hide main insight window
                        sports_window = tk.Toplevel()
                        sports_window.configure(bg='lightpink')
                        sports_window.geometry('600x600')
                        sports_window.title('Sports Insight')

                        def back():
                            sports_window.destroy()       # close this submodule window
                            insight_window.deiconify()    # show main insight window

                        def sports_link():
                            webbrowser.open("https://www.youtube.com/results?search_query=exercise+recommendations+for+menstruation")

                        image = Image.open("bg4.jpg").resize((600, 900))
                        photo = ImageTk.PhotoImage(image)
                        background_label = ttk.Label(sports_window, image=photo)
                        background_label.image = photo
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        resulta = insight.sport_text()
                        sports_text = ttk.Label(sports_window, text=resulta, justify='center', wraplength=450)
                        sports_text.pack(pady=10)

                        ttk.Button(sports_window, text='Sports Recommendations', command=sports_link).pack(pady=5)
                        ttk.Button(sports_window, text='Back', command=back).pack(pady=5)


                    def foodmodule():
                        insight_window.withdraw()
                        food_window = tk.Toplevel()
                        food_window.configure(bg='lightpink')
                        food_window.geometry('600x620')
                        food_window.title('Food Insight')

                        def back():
                            food_window.destroy()
                            insight_window.deiconify()

                        def food_link():
                            webbrowser.open("https://www.youtube.com/watch?v=qgry0uCa_wM")

                        image = Image.open("bg5.jpg").resize((600, 900))
                        photo = ImageTk.PhotoImage(image)
                        background_label = tk.Label(food_window, image=photo)
                        background_label.image = photo
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        resultb = insight.food()
                        food_text = ttk.Label(food_window, text=resultb, justify='center', wraplength=450)
                        food_text.pack(pady=10)

                        ttk.Button(food_window, text='Food Recommendations', command=food_link).pack(pady=5)
                        ttk.Button(food_window, text='Back', command=back).pack(pady=5)

                        
                    def sleepmodule():
                        insight_window.withdraw()
                        sleep_window = tk.Toplevel()
                        sleep_window.configure(bg='lightpink')
                        sleep_window.geometry('600x620')
                        sleep_window.title('Sleep Insight')

                        def back():
                            sleep_window.destroy()
                            insight_window.deiconify()

                        def sleep_link():
                            webbrowser.open("https://www.youtube.com/watch?v=Cjee6sM1Pow")

                        image = Image.open("bg6.jpg").resize((600, 900))
                        photo = ImageTk.PhotoImage(image)
                        background_label = tk.Label(sleep_window, image=photo)
                        background_label.image = photo
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        resultc = insight.sleep()
                        sleep_text = ttk.Label(sleep_window, text=resultc, justify='center', wraplength=450)
                        sleep_text.pack(pady=10)

                        ttk.Button(sleep_window, text='Sleep Positions Recommendations', command=sleep_link).pack(pady=5)
                        ttk.Button(sleep_window, text='Back', command=back).pack(pady=5)

                    def mensusmodule():
                        from mensuration import mensus
                        mensus()

                    sports_button = ttk.Button(button_frame, text='Sports that are suitable for menstruation', command=sportsmodule)
                    sports_button.pack(padx=60, pady=10, fill='x', expand=True)
                    
                    food_button = ttk.Button(button_frame, text='Foods That Raise Your Mood', command=foodmodule)
                    food_button.pack(padx=60, pady=10, fill='x', expand=True)
                    
                    sleep_button = ttk.Button(button_frame, text='Menstrual Pain Disrupting Sleep? Here are the tips', command=sleepmodule)
                    sleep_button.pack(padx=60, pady=10, fill='x', expand=True)

                    mensus_button = ttk.Button(button_frame, text='Is Your Period Late?', command=mensusmodule)
                    mensus_button.pack(padx=60, pady=10, fill='x', expand=True)

                    button_back = ttk.Button(button_frame, text='Back', command= closedwindow2)
                    button_back.pack(padx=60, pady=10, fill='x', expand=True)

                    insight_window.mainloop()

                def editperiod():
                    next_window.withdraw()

                    def backedit():
                        window_editperiod.withdraw()
                        next_window.deiconify()

                    window_editperiod = tk.Toplevel()
                    window_editperiod.configure(bg='lightpink')
                    window_editperiod.geometry('750x700')
                    window_editperiod.resizable(False, False)
                    window_editperiod.title('Edit Period')

                    input_frame = ttk.Frame(window_editperiod)
                    input_frame.pack(fill='x', padx=70, expand=True)

                    label_date_of_last_mensus = ttk.Label(input_frame, text='Date of your last menstrual period: (DD-MM-YYYY)')
                    label_date_of_last_mensus.pack(padx=10, pady=10, fill='x', expand=True)
                    entry_date_of_last_mensus = ttk.Entry(input_frame, textvariable=result3)
                    entry_date_of_last_mensus.pack(padx=10, pady=10, fill='x', expand=True)

                    label_average = ttk.Label(input_frame, text='Average Duration of Your Menses (Days):')
                    label_average.pack(padx=10, pady=10, fill='x', expand=True)
                    entry_average = ttk.Entry(input_frame, textvariable=result4)
                    entry_average.pack(padx=10, pady=10, fill='x', expand=True)

                    def save_data():
                        date = result3.get()
                        average = result4.get()
                        file_name = 'data_input.csv'
                        save_to_csv(date,average,file_name)

                    def check1():
                        try:
                            if result3.get().isalpha():
                                raise ValueError('Enter according to format!!')
                        except ValueError:
                            messagebox.showerror('Error')
                            editperiod()

                    def check2():
                        try:
                            if int(result4.get()) == result4.get():
                                raise ValueError('Enter Numbers Only!!')
                        except ValueError:
                            messagebox.showerror('Error')
                            editperiod()

                    from INPUT_and_EDIT_PERIOD import mensus
                    def count_mensus():
                        save_data()
                        mensus()

                    button_next = ttk.Button(input_frame, text='count', command=lambda: (count_mensus(), check1(), check2()))
                    button_next.pack()

                    button_backedit = ttk.Button(input_frame, text='Back', command=backedit)
                    button_backedit.pack()

                    window_editperiod.mainloop()

                next_window = tk.Toplevel()
                next_window.configure(bg='lightpink')
                next_window.geometry('750x700')
                next_window.resizable(False, False)
                next_window.title('Choose ur destination')

                button_frame = ttk.Frame(next_window)
                button_frame.pack(padx=60, pady=10, fill='x', expand=True)

                from calender import calender
                calender_module = calender
                calender_button = ttk.Button(button_frame, text='Calender', command=calender_module)
                calender_button.pack(padx=60, pady=10, fill='x', expand=True)
                
                button_insight = ttk.Button(button_frame, text='Insight', command=insightmodule)
                button_insight.pack(padx=60, pady=10, fill='x', expand=True)

                button_editperiod = ttk.Button(button_frame, text='Edit Period', command=editperiod)
                button_editperiod.pack(padx=60, pady=10, fill='x', expand=True)

                button_back = ttk.Button(button_frame, text='Back', command= closedwindow1)
                button_back.pack(padx=60, pady=10, fill='x', expand=True)

                next_window.mainloop()
                
            button_next = ttk.Button(main_window, text='Next', command=next_page)
            button_next.pack(fill='x', pady=10, expand=True)

            main_window.mainloop()
            break
        finally:
            main_window.destroy()
            main_program()
main_program()  
