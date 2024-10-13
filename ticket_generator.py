import csv
import json

class TicketGenerator:
    def __init__(self, tickets):
        self.tickets = tickets

    def ticket_generator(self):
        for ticket in self.tickets:
            yield ticket

    def to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['text', 'extra_questions', 'signed_by_dean']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for ticket in self.ticket_generator():
                writer.writerow({
                    'text': ticket.text,
                    'extra_questions': ','.join(ticket.extra_questions),
                    'signed_by_dean': ticket.signed_by_dean
                })

    def to_json(self, filename):
        with open(filename, 'w') as jsonfile:
            json.dump([ticket.__dict__ for ticket in self.ticket_generator()], jsonfile, indent=4)
