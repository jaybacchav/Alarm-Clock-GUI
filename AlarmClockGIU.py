import tkinter as tk
import datetime
import time
import winsound  # For Windows systems

def set_alarm():
    alarm_time = entry.get()  # Get the alarm time from the entry field
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")  # Get the current time
        if current_time == alarm_time:
            # Play sound when the alarm time matches the current time
            winsound.Beep(1000, 500)  # Change frequency and duration as needed for the beep sound
            break

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create and place entry field for alarm time
entry = tk.Entry(root, font=("Arial", 18))
entry.pack(padx=20, pady=20)

# Create and place set alarm button
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(padx=20, pady=10)

# Run the main loop
root.mainloop()
