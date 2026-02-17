### HELPER FUNCTIONS ###

# ROUND TO NEAREST HOUR FUNCTION
from datetime import datetime, timedelta


def round_to_nearest_hour(dt_object: datetime):
    """
    Rounds a datetime object to the nearest hour.
    Rounds up if the minute is 30 or greater, otherwise rounds down.
    format dt_object : "%d-%m-%Y %H:%M"
    """
    if dt_object.minute >= 30:
        # Round up to the next hour
        rounded_time = dt_object.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    else:
        # Round down to the current hour
        rounded_time = dt_object.replace(minute=0, second=0, microsecond=0)

    return rounded_time


# CONVERTING DURATION FUNCTION
def convert_into_minutes_duration(duration: datetime):
    """
    converting a timestamp duration (02:00:29) into rounded minutes duration (120 minutes)
    """
    hours = duration.hour * 60
    minutes = duration.minute
    seconds = duration.second / 60
    new_minutes_duration = round(hours + minutes + seconds)

    return new_minutes_duration


# CONVERTING DURATION FUNCTION
def convert_into_seconds_duration(duration: datetime):
    """
    converting a timestamp duration (00:02:00) into rounded seconds duration (120 seconds)
    """
    hours = duration.hour * 1200
    minutes = duration.minute * 60
    seconds = duration.second
    new_seconds_duration = round(minutes + seconds)

    return new_seconds_duration


# CONVERT FLOATED NUMBERS FUNCTION
def convert_floated_numbers(float_num: float):
    """
    converting float numbers (1.204, 995.000) into the right format (1204, 995)
    """
    result = 0
    new_format = round(float_num, 3) * 1000
    if new_format > 10000:
        result += new_format / 1000
    elif new_format % 1000 == 0:
        result += new_format / 1000
    else:
        result += new_format

    return int(result)


# CONVERT OLD FORMATTED SALES
def convert_sales(sales_str: str):
    """
    convert old formatted sales (Rp15.425.874) into a new one (15425874)
    """
    # remove Rp & "."
    new_format = float(sales_str.replace(".", "").replace("Rp", ""))

    return new_format


# CONVERT DURATION TIKTOK
def convert_duration_tiktok(duration: str):
    """
    to convert old formatted duration (3h 0min) into a new one (180 minutes)
    """
    hour = int(duration.split("h")[0]) * 60
    minutes = int(duration.split("h")[1].strip().split('min')[0])
    new_duration_format = hour + minutes

    return new_duration_format
