import tkinter as tk
from tkinter import messagebox
import time

# BMI Calculator
def calculate_bmi(result_label=None):
    height = float(height_entry.get()) / 100
    weight = float(weight_entry.get())
    bmi = weight / (height * height)
    result_label.config(text=f"BMI: {bmi:.2f}")


    if bmi < 18.5:
        messagebox.showinfo("BMI INFO", "BMI low,underweight")
    elif 25 <= bmi <= 29.9:
        messagebox.showinfo("BMI INFO", "BMI high, risk of obesity")
    elif bmi >= 30:
        messagebox.showinfo("BMI INFO", "BMI super high, obese")
    else:
        messagebox.showinfo("BMI INFO", "BMI normal")


# Fitness Tracker
workouts = []

def add_workout():
    exercise = exercise_entry.get()
    duration = duration_entry.get()
    if exercise and duration:
        workouts.append((exercise, int(duration)))
        update_workouts()
    else:
        messagebox.showwarning("Invalid Input", "Please enter both exercise and duration.")

def update_workouts():
    workouts_listbox.delete(0, tk.END)
    for ex, dur in workouts:
        workouts_listbox.insert(tk.END, f"{ex}: {dur} minutes")
    update_total_duration()

def update_total_duration():
    total_dur = sum(dur for _, dur in workouts)
    total_duration_label.config(text=f"Total Duration: {total_dur} minutes")




# Stop Watch
def start_stopwatch():
    global stopwatch_running
    stopwatch_running = True
    start_time = time.time()
    update_stopwatch(start_time)

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_running
    stopwatch_running = False
    stopwatch_label.config(text="00:00:00")

def update_stopwatch(start_time):
    if stopwatch_running:
        elapsed_time = time.time() - start_time
        hours, remainder = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        stopwatch_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        app.after(1000, update_stopwatch, start_time)

app = tk.Tk()
app.geometry("1000x1200")
app.title("Health and Fitness App")

# BMI Calculator Section
bmi_frame = tk.Frame(app, padx=14, pady=10, background="wheat")
bmi_frame.pack()
bmi_label = tk.Label(bmi_frame, text="BMI Calculator", font=("algerian", 22), fg="red")
bmi_label.pack()

height_label = tk.Label(bmi_frame, text="Height (cm):", fg="purple")
height_label.pack()
height_entry = tk.Entry(bmi_frame, fg="purple")
height_entry.pack()

weight_label = tk.Label(bmi_frame, text="Weight (kg):", fg="purple")
weight_label.pack()
weight_entry = tk.Entry(bmi_frame, fg="tomato")
weight_entry.pack()

calculate_button = tk.Button(bmi_frame, text="Calculate BMI", command=calculate_bmi, fg="red")
calculate_button.pack()



# Fitness Tracker Section
fitness_frame = tk.Frame(app, padx=10, pady=10, background="chocolate")
fitness_frame.pack()
fitness_label = tk.Label(fitness_frame, text="Fitness Tracker", font=("Algerian", 16), fg="red")
fitness_label.pack()

exercise_label = tk.Label(fitness_frame, text="Exercise:", fg="black")
exercise_label.pack()
exercise_entry = tk.Entry(fitness_frame, fg="red")
exercise_entry.pack()

duration_label = tk.Label(fitness_frame, text="Duration (minutes):", background="red", fg="black",)
duration_label.pack()
duration_entry = tk.Entry(fitness_frame, fg="purple")
duration_entry.pack()

add_workout_button = tk.Button(fitness_frame, text="Add Workout", command=add_workout, activeforeground="yellow", fg="purple")
add_workout_button.pack()

def clear_entries():
    exercise = exercise_entry.delete(0, tk.END)
    duration = duration_entry.delete(0, tk.END)
remove_workout_button = tk.Button(fitness_frame, text="Clear Entries", command=clear_entries)
remove_workout_button.pack()



workouts_listbox = tk.Listbox(fitness_frame, selectmode=tk.SINGLE, background="azure")
workouts_listbox.pack()



total_duration_label = tk.Label(fitness_frame, text="Total Duration: 0 minutes", fg="black")
total_duration_label.pack()

# Stop Watch Section
stopwatch_frame = tk.Frame(app, padx=5, pady=5, background="wheat")
stopwatch_frame.pack()
stopwatch_label = tk.Label(stopwatch_frame, text="00:00:00", font=("bauhaus93", 20), fg="black")
stopwatch_label.pack()

start_button = tk.Button(stopwatch_frame, text="Start", command=start_stopwatch, fg="black")
start_button.pack()

stop_button = tk.Button(stopwatch_frame, text="Stop", command=stop_stopwatch,fg="black")
stop_button.pack()

reset_button = tk.Button(stopwatch_frame, text="Reset", command=reset_stopwatch, fg="black")
reset_button.pack()

# Initialize stopwatch state
stopwatch_running = False

app.mainloop()
