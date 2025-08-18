Time Tracker App
---

### Introduction
Time Tracker App. It works with a CSV file, and it stores data on the time we've for different clients. When the app is run, it loads data from the CSV and presents users with a menu.
Utilities:
- Start tracking time we're spending on project for a client (which is reflected in the CSV)
- Stop tracking time on a project we're currently working on (also reflected in the CSV)
- Calculate the total times spent per client by entering their ID when prompted
  - choose a specific date range
  - Or within the X number of days
  - Or simply retrieve all the data from that client



### Getting started:
1. Create a virtual environment for this project
2. Install dateutil

### Extra challenges
- Create a helper function that returns "now" as a datetime string. Both `start_tracking()` and `stop_tracking()` can use this
- In `display_range_totals()`, it's possible that the user used an invalid date string. Catch any exceptions
- Create one function used to take a client and client job list to calculate and display data.
- Use list comprehension, `filter()`, and `lambda` to filter through client jobs and date ranges
---
