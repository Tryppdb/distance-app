import json  # swapped csv to json for easier use later with API
from rich import print
from datetime import datetime


LOG_FILE = "range_card.json"


def write_logfile(data: dict):
    # No need to check if LOG_FILE exists -- we'll
    # overwrite it regardless.
    with open(LOG_FILE, "w", newline="") as file:
        json.dump(data, file, indent=4)
    print(f"{data}")


def user_prompt():
    data = []
    distance = input("Distance to target (yds): ")
    wind_speed = input("Wind speed (mph): ")
    wind_direction = input("Wind direction (dms): ")
    temperature = input("Temperature (F): ")
    location = input("Location: ")
    notes = input("Notes: ")
    timestamp = datetime.now()
    inputs = [
        distance,
        wind_speed,
        wind_direction,
        temperature,
        location,
        notes,
        timestamp,
    ]

    # Now we've got all the user's information, loop through the list and return
    # floats where necessary.

    for i in inputs:
        try:
            data.append(float(i))
        except (ValueError, TypeError):
            data.append(i)

    # We'll use a dict here instead of a list, so we can have
    # `key: value` pairs, and later call them by key if desired.
    log_data = {
        "timestamp": data[6].strftime("%d-%m-%Y %H:%M"),
        "distance": data[0],
        "wind speed": data[1],
        "wind direction": data[2],
        "temperature": data[3],
        "location": data[4],
        "notes": data[5],
    }
    return log_data


if __name__ == "__main__":
    write_logfile(user_prompt())
