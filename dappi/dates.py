from datetime import date, datetime
import calendar
from .message import *
from .user import * 
from .dates import *

DATES = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12",
}


def get_date_time_from_string(date_string):
    # date_string = date_string.replace("-", "")
    date_string = insert_century(date_string)
    # date_string = remove_am_pm(date_string)
    date_string = convert_month_abbreviation_to_month_index(date_string)
    date_string = date_string.strip()
    return datetime.strptime(date_string, "%d-%m-%Y %I:%M %p")


def convert_month_abbreviation_to_month_index(date_string):
    abbreviation_index = date_string.find("-") + 1
    abbreviation = get_abbreviation_from_index(date_string, abbreviation_index)
    date_string = delete_abbreviation_from_date_string(date_string, abbreviation)
    if abbreviation in DATES:
        month_index = list(calendar.month_abbr).index(abbreviation)
        return (
            date_string[:abbreviation_index]
            + f"{month_index}"
            + date_string[abbreviation_index:]
        )


def delete_abbreviation_from_date_string(date_string, abbreviation):
    date_string = date_string.replace(abbreviation, "")
    return date_string


def get_abbreviation_from_index(date_string, abbreviation_index):
    return (
        date_string[abbreviation_index]
        + date_string[abbreviation_index + 1]
        + date_string[abbreviation_index + 2]
    )


def insert_century(date_string):
    year_dash_index = date_string.rfind("-") + 1
    return date_string[:year_dash_index] + "20" + date_string[year_dash_index:]


def remove_am_pm(date_string):
    date_string = date_string.replace("AM", "")
    date_string = date_string.replace("PM", "")
    return date_string
