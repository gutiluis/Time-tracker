import csv
import utils
import datetime # used with datetime.datetime.now()
from dateutil import relativedelta



# gather details from the user about the client and job description. and then use it in the menus.py script
def start_tracking(client, description):
    print(f"Start tracking {description} for {client}")

    now = datetime.datetime.now()

    format_string = "%I:%M%p %Y-%m-%d"

    start_time = datetime.datetime.strftime(now, format_string)

    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='')
        writer.writerow([client, description, start_time, ''])

def stop_tracking():
    print("Stopping tracking")

    now = datetime.datetime.now()
    format_string = "%I:%M%p %Y-%m-%d"

    end_time = datetime.datetime.strftime(now, format_string)
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([end_time])


def display_all_totals(client):
    print(f"Calculating time spent on all jobs for {client}...")
# get_by_client from utils.py file
    client_jobs = utils.get_by_client(client)
    total = relativedelta.relativedelta()

    for job in client_jobs:
        format_string = "%I:%M%p %Y-%m-%d"
        start_dt = datetime.datetime.strptime(job["start_time"], format_string)
        end_dt = datetime.datetime.strptime(job["end_time"], format_string)
        time_spent = relativedelta.relativedelta(end_dt, start_dt)

        print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")
        total += time_spent
        # print out job itselt
# add time spent to the total
    print(f"Total for {client}") # total is a relativedelta object
#    print(f"X hours x minutes") # acces the hours/minutes of the relativedelta object directly
    print(f"{total.hours} hours {total.minutes} minutes")


# when the user decides to input a date range
def display_range_totals(client, dates_str_list):
    print(f"Calculating time spent on jobs for {client} in the specified range...")
    client_jobs = utils.get_by_client(client)
    format_string = "%Y-%m-%d"
    range_start_dt = datetime.datetime.strptime(dates_str_list[0], format_string)
    range_end_dt = datetime.datetime.strptime(dates_str_list[1], format_string).replace(hour=23, minute=59, second=59)
    total = relativedelta.relativedelta()
    for job in client_jobs:
        format_string_dt = "%I:%M%p %Y-%m-%d"
        job_end_dt = datetime.datetime.strptime(job['end_time'], format_string_dt)
        if range_end_dt > job_end_dt > range_start_dt: 
            job_start_dt = datetime.datetime.strptime(job['start_time'], format_string_dt)
            time_spent = relativedelta.relativedelta(job_end_dt, job_start_dt)
            print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")
            total += time_spent
    print(f"Total for {client}")
    print(f"{total.hours} hours {total.minutes} minutes")


def display_x_days_totals(client, days):
    print(f"Calculating time spent on jobs for {client} in the last {days} days...")
    client_jobs = utils.get_by_client(client)
    go_back = relativedelta.relativedelta(days=days)
    range_start_dt = datetime.datetime.now() - go_back
    range_end_dt = datetime.datetime.now()
    total = relativedelta.relativedelta()
    for job in client_jobs:
        job_end_dt = datetime.datetime.strptime(job['end_time'], "%I:%M%p %Y-%m-%d")
        if range_end_dt > job_end_dt > range_start_dt:
            job_start_dt = datetime.datetime.strptime(job['start_time'], "%I:%M%p %Y-%m-%d")
            time_spent = relativedelta.relativedelta(job_end_dt, job_start_dt)
            print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")
            total += time_spent

    print(f"Total for {client}")
    print(f"{total.hours} hours {total.minutes} minutes")
