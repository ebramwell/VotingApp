#some of this code was generated from AI. I reviewed and edited it for the assignment requirements.

import csv
from typing import Dict

class VoteManager:
    """
    Manages voting data, ensures no double voting, 
    and handles CSV file.
    """

    def __init__(self):
        self.votes: Dict[str, int] = {
            "Isabella": 0,
            "Genji": 0,
            "Hannah": 0
        }
        self.voted_for: set[str] = set()
        self.load_votes()

    def load_votes(self) -> None:
        """this loads previous vote counts from CSV if it exists."""
        try:
            with open("votes.csv", "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                for row in reader:
                    name, count = row
                    self.votes[name] = int(count)
        except FileNotFoundError:
            pass  # no file yet

    def save_votes(self) -> None:
        """Saves all vote counts to CSV."""
        with open("votes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["candidate", "votes"])
            for name, count in self.votes.items():
                writer.writerow([name, count])

    def vote(self, name: str) -> bool:
        """
        Attempts to register a vote.
        Returns True if successful, False if already voted for this candidate.
        """
        if name in self.voted_for:
            return False

        self.voted_for.add(name)
        self.votes[name] += 1
        return True

    def total_votes(self) -> int:
        return sum(self.votes.values())
