import datetime
import tkinter as tk

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")
        self.current_time_label = tk.Label(self.master, font=("Arial", 24))
        self.current_time_label.pack(pady=20)
        self.set_alarm_button = tk.Button(self.master, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)
        self.alarm_time_label = tk.Label(self.master, font=("Arial", 24))
        self.alarm_time_label.pack(pady=20)
        self.alarm_set = False
        self.alarm_time = None
        self.check_alarm()

    def set_alarm(self):
        self.alarm_set = True
        self.alarm_time = tk.simpledialog.askstring("Set Alarm", "Enter time in HH:MM format:")
        self.alarm_time_label.config(text=f"Alarm set for {self.alarm_time}")

    def check_alarm(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        self.current_time_label.config(text=f"Current time: {current_time}")
        if self.alarm_set and current_time == self.alarm_time:
            tk.messagebox.showinfo("Alarm", "Time to wake up!")
            self.alarm_set = False
            self.alarm_time = None
            self.alarm_time_label.config(text="")

        self.master.after(1000, self.check_alarm)

root = tk.Tk()
alarm_clock = AlarmClock(root)
root.mainloop()
