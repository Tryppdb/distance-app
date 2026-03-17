import csv
import os
from datetime import datetime


LOG_FILE = "log.csv"


def create_log_file_if_needed():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "distance_meters",
                "wind_speed_mph",
                "wind_direction",
                "temperature_f",
                "location",
                "notes"
            ])


def get_float_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def get_text_input(prompt):
    return input(prompt).strip()


def save_entry(data):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


def main():
    create_log_file_if_needed()

    print("Range Session Logger")
    print("--------------------")

    distance = get_float_input("Enter measured distance (meters): ")
    wind_speed = get_float_input("Enter wind speed (mph): ")
    wind_direction = get_text_input("Enter wind direction: ")
    temperature = get_float_input("Enter temperature (F): ")
    location = get_text_input("Enter location: ")
    notes = get_text_input("Enter notes: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = [
        timestamp,
        distance,
        wind_speed,
        wind_direction,
        temperature,
        location,
        notes
    ]

    save_entry(entry)

    print("\nSession saved successfully!")
    print("---------------------------")
    print(f"Time: {timestamp}")
    print(f"Distance: {distance} meters")
    print(f"Wind Speed: {wind_speed} mph")
    print(f"Wind Direction: {wind_direction}")
    print(f"Temperature: {temperature} F")
    print(f"Location: {location}")
    print(f"Notes: {notes}")


if __name__ == "__main__":
    main()