class Ticket:
    def __init__(
        self,
        title,
        description,
        issue_type,
        status="Open",
        created_at=None,
        resolved_at=None,
        resolution_notes=None,
        ticket_id=None
    ):
        self.id = ticket_id
        self.title = title
        self.description = description
        self.issue_type = issue_type
        self.status = status
        self.created_at = created_at
        self.resolved_at = resolved_at
        self.resolution_notes = resolution_notes

    def __str__(self):
        return (
            f"Ticket ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Issue Type: {self.issue_type}\n"
            f"Status: {self.status}\n"
            f"Created At: {self.created_at}\n"
            f"Resolved At: {self.resolved_at}\n"
            f"Resolution Notes: {self.resolution_notes}\n"
        )
