from datetime import datetime

def is_past_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")  # Convert the string to a datetime object
    return date < datetime.now()  # Check if the date is in the past

date_strings = ["2023-12-10", "2024-12-20", "2024-01-01", "2025-03-15", "2024-12-10"]

valid_dates = list(filter(is_past_date, date_strings))

print("Dates in the past:", valid_dates)
