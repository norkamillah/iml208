import tkinter as tk
from tkinter import messagebox

class GymBookingSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Booking System")

        self.label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.label_date.grid(row=0, column=0)
        self.entry_date = tk.Entry(root)
        self.entry_date.grid(row=0, column=1)

        self.label_time = tk.Label(root, text="Time (HH:MM):")
        self.label_time.grid(row=1, column=0)
        self.entry_time = tk.Entry(root)
        self.entry_time.grid(row=1, column=1)

        self.label_user = tk.Label(root, text="User ID:")
        self.label_user.grid(row=2, column=0)
        self.entry_user = tk.Entry(root)
        self.entry_user.grid(row=2, column=1)

        self.button_create = tk.Button(root, text="Create Session", command=self.create_session)
        self.button_create.grid(row=3, column=0, columnspan=2, pady=5)

        self.button_view = tk.Button(root, text="View Session", command=self.view_session)
        self.button_view.grid(row=4, column=0, columnspan=2, pady=5)

        self.button_book = tk.Button(root, text="Book Session", command=self.book_session)
        self.button_book.grid(row=5, column=0, columnspan=2, pady=5)

        self.button_update = tk.Button(root, text="Update Session", command=self.update_session)
        self.button_update.grid(row=6, column=0, columnspan=2, pady=5)

        self.button_cancel = tk.Button(root, text="Cancel Session", command=self.cancel_session)
        self.button_cancel.grid(row=7, column=0, columnspan=2, pady=5)

        self.text_display = tk.Text(root, height=50, width=100)
        self.text_display.grid(row=8, column=0, columnspan=2, pady=10)

        # Color configuration
        self.bg_color = "#FFF8DC"
        self.button_bg_color = "#545454"
        self.button_fg_color = "#ffffff"
        self.label_color = "#333333"
        self.entry_color = "#666666"
        self.text_color = "#121212"

        self.root.config(bg=self.bg_color)

        # Labels
        self.label_date = tk.Label(root, text="Date (YYYY-MM-DD):", bg=self.bg_color, fg=self.label_color)
        self.label_date.grid(row=0, column=0)
        self.label_time = tk.Label(root, text="Time (HH:MM):", bg=self.bg_color, fg=self.label_color)
        self.label_time.grid(row=1, column=0)
        self.label_user = tk.Label(root, text="User ID:", bg=self.bg_color, fg=self.label_color)
        self.label_user.grid(row=2, column=0)

        # Entries
        self.entry_date = tk.Entry(root, bg=self.entry_color)
        self.entry_date.grid(row=0, column=1)
        self.entry_time = tk.Entry(root, bg=self.entry_color)
        self.entry_time.grid(row=1, column=1)
        self.entry_user = tk.Entry(root, bg=self.entry_color)
        self.entry_user.grid(row=2, column=1)

        # Buttons
        self.button_create = tk.Button(root, text="Create Session", command=self.create_session,
                                       bg=self.button_bg_color, fg=self.button_fg_color)
        self.button_create.grid(row=3, column=0, columnspan=10, pady=15)
        self.button_view = tk.Button(root, text="View Session", command=self.view_session,
                                     bg=self.button_bg_color, fg=self.button_fg_color)
        self.button_view.grid(row=4, column=0, columnspan=10, pady=15)
        self.button_book = tk.Button(root, text="Book Session", command=self.book_session,
                                     bg=self.button_bg_color, fg=self.button_fg_color)
        self.button_book.grid(row=5, column=0, columnspan=10, pady=15)
        self.button_update = tk.Button(root, text="Update Session", command=self.update_session,
                                       bg=self.button_bg_color, fg=self.button_fg_color)
        self.button_update.grid(row=6, column=0, columnspan=10, pady=15)
        self.button_cancel = tk.Button(root, text="Cancel Session", command=self.cancel_session,
                                       bg=self.button_bg_color, fg=self.button_fg_color)
        self.button_cancel.grid(row=7, column=0, columnspan=10, pady=15)

        # Text Display
        self.text_display = tk.Text(root, height=50, width=40, bg=self.bg_color, fg=self.text_color)
        self.text_display.grid(row=8, column=0, columnspan=10, pady=20)

        self.booking_system = GymBookingSystem()

    def create_session(self):
        date = self.entry_date.get()
        time = self.entry_time.get()
        self.booking_system.create_session(date, time)
        self.update_display()

    def view_session(self):
        date = self.entry_date.get()
        time = self.entry_time.get()
        result = self.booking_system.read_session(date, time)
        self.text_display.insert(tk.END, result + "\n")

    def book_session(self):
        date = self.entry_date.get()
        time = self.entry_time.get()
        user_id = self.entry_user.get()
        self.booking_system.book_session(user_id, date, time)
        self.update_display()

    def update_session(self):
        date = self.entry_date.get()
        time = self.entry_time.get()
        user_id = self.entry_user.get()
        self.booking_system.update_session(user_id, date, time)
        self.update_display()

    def cancel_session(self):
        date = self.entry_date.get()
        time = self.entry_time.get()
        self.booking_system.cancel_session(date, time)
        self.update_display()

    def update_display(self):
        self.text_display.delete(1.0, tk.END)
        booked_sessions = self.booking_system.view_booked_sessions()
        for session in booked_sessions:
            self.text_display.insert(tk.END, session + "\n")

class GymBookingSystem:
    def __init__(self):
        self.sessions = {}

    def book_session(self, user_id, session_date, session_time):
        if session_date not in self.sessions:
            self.sessions[session_date] = {}
        if session_time not in self.sessions[session_date]:
            self.sessions[session_date][session_time] = user_id
            messagebox.showinfo("Success", f"Session booked for user {user_id} on {session_date} at {session_time}.")
        else:
            messagebox.showwarning("Warning", "This session time is already booked. Please choose another time.")

    def view_booked_sessions(self):
        booked_sessions = []
        for date, times in self.sessions.items():
            for time, user_id in times.items():
                booked_sessions.append(f"Date: {date}, Time: {time}, User ID: {user_id}")
        return booked_sessions

    def update_session(self, user_id, session_date, session_time):
        if session_date in self.sessions and session_time in self.sessions[session_date]:
            self.sessions[session_date][session_time] = user_id
            messagebox.showinfo("Success", f"Session updated for user {user_id} on {session_date} at {session_time}.")
        else:
            messagebox.showwarning("Warning", "Session not found.")

    def cancel_session(self, session_date, session_time):
        if session_date in self.sessions and session_time in self.sessions[session_date]:
            del self.sessions[session_date][session_time]
            messagebox.showinfo("Success", f"Session canceled for {session_date} at {session_time}.")
        else:
            messagebox.showwarning("Warning", "Session not found.")

    def create_session(self, session_date, session_time):
        if session_date not in self.sessions:
            self.sessions[session_date] = {}
        if session_time not in self.sessions[session_date]:
            self.sessions[session_date][session_time] = None
            messagebox.showinfo("Success", f"Session created on {session_date} at {session_time}.")
        else:
            messagebox.showwarning("Warning", "This session time already exists.")

    def read_session(self, session_date, session_time):
        if session_date in self.sessions and session_time in self.sessions[session_date]:
            user_id = self.sessions[session_date][session_time]
            if user_id:
                return f"Session on {session_date} at {session_time} booked by user: {user_id}"
            else:
                return f"Session on {session_date} at {session_time} available."
        else:
            return "Session not found."

def main():
    root = tk.Tk()
    app = GymBookingSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

