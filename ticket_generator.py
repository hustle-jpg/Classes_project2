import csv
import json

class TicketGenerator:
    def __init__(self, tickets):
        self.tickets = tickets

    def to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['text', 'extra_questions', 'signed_by_dean']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for ticket in self.tickets:
                writer.writerow({
                    'text': ticket.text,
                    'extra_questions': ','.join(ticket.extra_questions),
                    'signed_by_dean': ticket.signed_by_dean
                })

    def to_json(self, filename):
        with open(filename, 'w') as jsonfile:
            json.dump([ticket.__dict__ for ticket in self.tickets], jsonfile, indent=4)
