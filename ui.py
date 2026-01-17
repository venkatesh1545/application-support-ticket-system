import tkinter as tk
from tkinter import messagebox, scrolledtext

from ticket_service import (
    create_ticket,
    get_all_tickets,
    update_ticket_status,
    resolve_ticket
)


class TicketSystemUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Support Ticket System")
        self.root.geometry("600x500")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Support Ticket System", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(self.root, text="Create Ticket", width=25, command=self.open_create_ticket).pack(pady=5)
        tk.Button(self.root, text="View All Tickets", width=25, command=self.view_tickets).pack(pady=5)
        tk.Button(self.root, text="Update Ticket Status", width=25, command=self.open_update_status).pack(pady=5)
        tk.Button(self.root, text="Resolve Ticket", width=25, command=self.open_resolve_ticket).pack(pady=5)
        tk.Button(self.root, text="Exit", width=25, command=self.root.quit).pack(pady=10)

    # -------- Create Ticket --------
    def open_create_ticket(self):
        window = tk.Toplevel(self.root)
        window.title("Create Ticket")
        window.geometry("400x300")

        tk.Label(window, text="Title").pack()
        title_entry = tk.Entry(window, width=40)
        title_entry.pack()

        tk.Label(window, text="Description").pack()
        desc_entry = tk.Entry(window, width=40)
        desc_entry.pack()

        tk.Label(window, text="Issue Type (Bug/Error/Request)").pack()
        issue_entry = tk.Entry(window, width=40)
        issue_entry.pack()

        def submit():
            if not title_entry.get() or not desc_entry.get() or not issue_entry.get():
                messagebox.showerror("Error", "All fields are required")
                return

            create_ticket(title_entry.get(), desc_entry.get(), issue_entry.get())
            messagebox.showinfo("Success", "Ticket created successfully")
            window.destroy()

        tk.Button(window, text="Submit", command=submit).pack(pady=10)

    # -------- View Tickets --------
    def view_tickets(self):
        window = tk.Toplevel(self.root)
        window.title("All Tickets")
        window.geometry("700x400")

        text_area = scrolledtext.ScrolledText(window, width=80, height=20)
        text_area.pack()

        tickets = get_all_tickets()
        if not tickets:
            text_area.insert(tk.END, "No tickets found.")
            return

        for ticket in tickets:
            text_area.insert(tk.END, str(ticket))
            text_area.insert(tk.END, "-" * 50 + "\n")

    # -------- Update Status --------
    def open_update_status(self):
        window = tk.Toplevel(self.root)
        window.title("Update Ticket Status")
        window.geometry("400x250")

        tk.Label(window, text="Ticket ID").pack()
        id_entry = tk.Entry(window)
        id_entry.pack()

        tk.Label(window, text="New Status (Open/In Progress/Resolved)").pack()
        status_entry = tk.Entry(window)
        status_entry.pack()

        def submit():
            try:
                update_ticket_status(int(id_entry.get()), status_entry.get())
                messagebox.showinfo("Success", "Status updated successfully")
                window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(window, text="Update", command=submit).pack(pady=10)

    # -------- Resolve Ticket --------
    def open_resolve_ticket(self):
        window = tk.Toplevel(self.root)
        window.title("Resolve Ticket")
        window.geometry("400x250")

        tk.Label(window, text="Ticket ID").pack()
        id_entry = tk.Entry(window)
        id_entry.pack()

        tk.Label(window, text="Resolution Notes").pack()
        notes_entry = tk.Entry(window, width=40)
        notes_entry.pack()

        def submit():
            try:
                resolve_ticket(int(id_entry.get()), notes_entry.get())
                messagebox.showinfo("Success", "Ticket resolved successfully")
                window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(window, text="Resolve", command=submit).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicketSystemUI(root)
    root.mainloop()
