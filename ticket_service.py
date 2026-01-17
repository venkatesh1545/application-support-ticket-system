from datetime import datetime
from database import get_connection
from models import Ticket


def create_ticket(title, description, issue_type):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO tickets (title, description, issue_type, status, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (title, description, issue_type, "Open", created_at))

    conn.commit()
    conn.close()


def get_all_tickets():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    rows = cursor.fetchall()
    conn.close()

    tickets = []
    for row in rows:
        tickets.append(
            Ticket(
                ticket_id=row[0],
                title=row[1],
                description=row[2],
                issue_type=row[3],
                status=row[4],
                created_at=row[5],
                resolved_at=row[6],
                resolution_notes=row[7]
            )
        )
    return tickets


def get_tickets_by_status(status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets WHERE status = ?", (status,))
    rows = cursor.fetchall()
    conn.close()

    tickets = []
    for row in rows:
        tickets.append(
            Ticket(
                ticket_id=row[0],
                title=row[1],
                description=row[2],
                issue_type=row[3],
                status=row[4],
                created_at=row[5],
                resolved_at=row[6],
                resolution_notes=row[7]
            )
        )
    return tickets


def update_ticket_status(ticket_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tickets
        SET status = ?
        WHERE id = ?
    """, (new_status, ticket_id))

    conn.commit()
    conn.close()


def resolve_ticket(ticket_id, resolution_notes):
    conn = get_connection()
    cursor = conn.cursor()

    resolved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE tickets
        SET status = ?, resolved_at = ?, resolution_notes = ?
        WHERE id = ?
    """, ("Resolved", resolved_at, resolution_notes, ticket_id))

    conn.commit()
    conn.close()
