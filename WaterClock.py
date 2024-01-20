# Import PySimpleGUI and datetime
import PySimpleGUI as sg
import datetime

# Define the layout of the app
layout = [
    [
        sg.Text("12hr Time:", font="Helvetica 15", justification="center"),
        sg.Text("", key="-time12-", font="Helvetica 40", justification="center"),
    ],
    [
        sg.Text("24hr Time:", font="Helvetica 15", justification="center"),
        sg.Text("", key="-time24-", font="Helvetica 40", justification="center"),
    ],
    [sg.Exit(size=(10, 3))],
]

# Create a window to display the layout
window = sg.Window("WaterClock", layout, size=(600, 200))




# Define a function to get the current time in 12hr format and return it
def now12():
    ntime = datetime.datetime.now()
    nt = ntime.strftime("%I:%M:%S %p")
    return nt


# Define a function to get the current time in 24hr format and return it
def now24():
    ntime = datetime.datetime.now()
    nt = ntime.strftime("%H:%M:%S")
    return nt


# Create a while loop to handle the events and values from the window
while True:
    event, values = window.read(timeout=10, timeout_key="-timeout-")
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    elif event == "-timeout-":
        # Update the text elements with the current time in 12hr and 24hr format
        window["-time12-"].update(now12())
        window["-time24-"].update(now24())

# Close the window
window.close()
