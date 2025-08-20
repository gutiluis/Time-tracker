Time Tracker App
---

### Introduction
Time Tracker App. Works with a comma-separated values(CSV) file, and it stores data on the time values of the clients. 

Current functions:
- Main menu
- Start tracking time spent per project for each client (which is reflected in the CSV)
- Stop tracking time on a current project (also reflected in the CSV)
- Calculate the total times spent per client by entering their ID when prompted
- Choose and print specific date ranges. Or within the X number of days. Or simply retrieve all the data from that client



### Getting started:
- python3 -m venv venv
- source venv/bin/activate
- sudo apt update && sudo apt upgrade
- sudo apt install dateutil
- python3 main.py


To do:
- Create a helper function that returns "now" as a datetime string. Both `start_tracking()` and `stop_tracking()` can use this
- In `display_range_totals()`, it's possible that the user used an invalid date string. Catch any exceptions
- Create one function used to take a client and client job list to calculate and display data.
- Use list comprehension, `filter()`, and `lambda` to filter through client jobs and date ranges
---
