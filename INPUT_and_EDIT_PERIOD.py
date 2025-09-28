from datetime import timedelta, datetime
import os
import calendar
import pandas as pd

def calculate_mensus_cycle(date, average):

    start_date_of_next_mensus = date + timedelta(days=28)
    end_date_of_next_mensus = date + timedelta(days=27 + average)

    start_date_of_next_follicular = end_date_of_next_mensus + timedelta(days=1)
    if average > 5:
        end_date_of_next_follicular = start_date_of_next_follicular + timedelta(days=6)
    else:
        end_date_of_next_follicular = start_date_of_next_follicular + timedelta(days=8)

    start_date_of_next_ovulation = end_date_of_next_follicular + timedelta(days=1)
    end_date_of_next_ovulation = end_date_of_next_follicular + timedelta(days=3)

    start_date_of_next_luteal = end_date_of_next_ovulation + timedelta(days=1)
    if average > 5:
        end_date_of_next_luteal = start_date_of_next_luteal + timedelta(days=8)
    else:
        end_date_of_next_luteal = start_date_of_next_luteal + timedelta(days=10)

    mensus_duration = average
    follicular_duration = (end_date_of_next_follicular - start_date_of_next_follicular  + timedelta(days=1)).days
    ovulation_duration = (end_date_of_next_ovulation - start_date_of_next_ovulation + timedelta(days=1)).days
    luteal_duration = (end_date_of_next_ovulation - start_date_of_next_luteal + timedelta(days=1)).days

    result = (
        start_date_of_next_mensus.date(),
        end_date_of_next_mensus.date(),
        start_date_of_next_follicular.date(),
        end_date_of_next_follicular.date(),
        start_date_of_next_ovulation.date(),
        end_date_of_next_ovulation.date(),
        start_date_of_next_luteal.date(),
        end_date_of_next_luteal.date(),
        mensus_duration,
        follicular_duration,
        ovulation_duration,
        luteal_duration,
        )

    return result


def save_to_csv_1(result, file_name):
    header = 'start date of mensus,end date of menses,start date of follicular,end date of follicular,start date of ovulation,end date of ovulation,start date of luteal,end date of ovule'
    template_csv = '\n{},{},{},{},{},{},{},{}'.format(
            result[0].strftime('%d-%m-%Y'),
            result[1].strftime('%d-%m-%Y'),
            result[2].strftime('%d-%m-%Y'),
            result[3].strftime('%d-%m-%Y'),
            result[4].strftime('%d-%m-%Y'),
            result[5].strftime('%d-%m-%Y'),
            result[6].strftime('%d-%m-%Y'),
            result[7].strftime('%d-%m-%Y'),
        )
    file_mensusdata = open(file_name, 'w')
    file_mensusdata.write(header)
    file_mensusdata.write(template_csv)
    file_mensusdata.close()

def save_to_csv_2(result, file_name):
    header = 'Month,Mensus Duration,Follicular Duration,Ovulation Duration,Luteal Duration'
    template_csv ='\n{},{},{},{},{}'.format(
        calendar.month_name[result[0].month], 
        result[8],
        result[9],
        result[10],
        result[11],
    )
    file_exists = os.path.isfile(file_name)
    file_mensusdata = open(file_name, 'a')
    if not file_exists:
        file_mensusdata.write(header)
    file_mensusdata.write(template_csv)
    file_mensusdata.close()


def mensus():
    df = pd.read_csv('data_input.csv')

    date = df['Date'].astype(str)
    average = int(df['Average'].values[0])
    date = pd.to_datetime(date, format='%d-%m-%Y').iloc[0]
    result = calculate_mensus_cycle(date, average)
    calculate_mensus_cycle(date, average)
    save_to_csv_1(result,'mensus_cycle.csv')
    save_to_csv_2(result,'duration_of_cycle.csv')
    estimation = result[0].day
    now = datetime.now()
    today = now.day
    difference = estimation-today
    if difference >=1:
        from calender import confirm
        confirm()
