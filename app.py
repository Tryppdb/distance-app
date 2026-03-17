import csv
import os
from datetime import datetime

import streamlit as st


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


def save_entry(row):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)


def load_entries():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        return []

    return rows[1:]


create_log_file_if_needed()

st.set_page_config(page_title="Distance App", page_icon="📘", layout="centered")

st.title("Distance App")
st.caption("Log session environment data locally")

with st.form("session_form"):
    distance = st.number_input("Measured Distance (meters)", min_value=0.0, step=1.0)
    wind_speed = st.number_input("Wind Speed (mph)", min_value=0.0, step=1.0)
    wind_direction = st.text_input("Wind Direction")
    temperature = st.number_input("Temperature (F)", step=1.0)
    location = st.text_input("Location")
    notes = st.text_area("Notes", placeholder="Example: uphill, warm day, steady wind")

    submitted = st.form_submit_button("Save Session")

if submitted:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [
        timestamp,
        distance,
        wind_speed,
        wind_direction.strip(),
        temperature,
        location.strip(),
        notes.strip()
    ]
    save_entry(row)
    st.success("Session saved successfully.")

st.divider()
st.subheader("Recent Entries")

entries = load_entries()

if not entries:
    st.info("No saved entries yet.")
else:
    headers = [
        "Timestamp",
        "Distance (m)",
        "Wind Speed (mph)",
        "Wind Direction",
        "Temperature (F)",
        "Location",
        "Notes"
    ]

    recent_entries = list(reversed(entries[-5:]))
    table_data = [dict(zip(headers, entry)) for entry in recent_entries]
    st.dataframe(table_data, use_container_width=True)