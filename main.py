from ticket_service import (
    create_ticket,
    get_all_tickets,
    get_tickets_by_status,
    update_ticket_status,
    resolve_ticket
)


def show_menu():
    print("\n===== Support Ticket System =====")
    print("1. Create new ticket")
    print("2. View all tickets")
    print("3. View tickets by status")
    print("4. Update ticket status")
    print("5. Resolve ticket")
    print("6. Exit")


def create_ticket_flow():
    title = input("Enter ticket title: ").strip()
    description = input("Enter ticket description: ").strip()
    issue_type = input("Enter issue type (Bug/Error/Request): ").strip()

    if not title or not description or not issue_type:
        print("All fields are required.")
        return

    create_ticket(title, description, issue_type)
    print("Ticket created successfully.")


def view_all_tickets_flow():
    tickets = get_all_tickets()
    if not tickets:
        print("No tickets found.")
        return

    for ticket in tickets:
        print(ticket)
        print("-" * 40)


def view_tickets_by_status_flow():
    status = input("Enter status (Open/In Progress/Resolved): ").strip()
    tickets = get_tickets_by_status(status)

    if not tickets:
        print(f"No tickets found with status '{status}'.")
        return

    for ticket in tickets:
        print(ticket)
        print("-" * 40)


def update_ticket_status_flow():
    try:
        ticket_id = int(input("Enter ticket ID: "))
        new_status = input("Enter new status (Open/In Progress/Resolved): ").strip()
        update_ticket_status(ticket_id, new_status)
        print("Ticket status updated successfully.")
    except ValueError:
        print("Invalid ticket ID.")


def resolve_ticket_flow():
    try:
        ticket_id = int(input("Enter ticket ID: "))
        resolution_notes = input("Enter resolution notes: ").strip()

        if not resolution_notes:
            print("Resolution notes cannot be empty.")
            return

        resolve_ticket(ticket_id, resolution_notes)
        print("Ticket resolved successfully.")
    except ValueError:
        print("Invalid ticket ID.")


def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            create_ticket_flow()
        elif choice == "2":
            view_all_tickets_flow()
        elif choice == "3":
            view_tickets_by_status_flow()
        elif choice == "4":
            update_ticket_status_flow()
        elif choice == "5":
            resolve_ticket_flow()
        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
