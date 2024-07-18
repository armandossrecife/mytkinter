import tkinter as tk

class Timer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timer")

        # StringVar to hold the current time
        self.current_time = tk.StringVar()
        self.current_time.set("00:00:00")

        # Label to display the time
        self.time_label = tk.Label(self, textvariable=self.current_time, font=("Arial", 100))
        self.time_label.pack(padx=10, pady=10)

        # Variables to track timer state and time elapsed
        self.is_running = False
        self.elapsed_time = 0

        # Button functions (start, stop, reset)
        self.start_button = tk.Button(self, text="Start", command=self.start_timer)
        self.start_button.pack(padx=5, pady=5)

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.pack(padx=5, pady=5)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_timer, state="disabled")
        self.reset_button.pack(padx=5, pady=5)

        # Update time every second
        self.update_clock()

    def update_clock(self):
        if self.is_running:
            self.elapsed_time += 1
            formatted_time = self.format_time(self.elapsed_time)
            self.current_time.set(formatted_time)
        self.after(1000, self.update_clock)

    def format_time(self, seconds):
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def start_timer(self):
        self.is_running = True
        self.stop_button.config(state="normal")
        self.reset_button.config(state="normal")
        self.start_button.config(state="disabled")

    def stop_timer(self):
        self.is_running = False
        self.stop_button.config(state="disabled")

    def reset_timer(self):
        self.is_running = False
        self.elapsed_time = 0
        self.current_time.set(self.format_time(self.elapsed_time))
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.start_button.config(state="normal")

if __name__ == "__main__":
    timer = Timer()
    timer.mainloop()