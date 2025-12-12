#some of this code was generated from AI. I reviewed and edited it for the assignment requirements.

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from vote_manager import VoteManager

class ResultsWindow(QWidget):
    """Window that shows vote results."""

    def __init__(self, manager: VoteManager):
        super().__init__()
        self.setWindowTitle("Voting Results")
        self.manager = manager

        layout = QVBoxLayout()

        #results text
        text = ""
        for name, count in manager.votes.items():
            text += f"{name}: {count} votes\n"

        text += f"\nTotal Votes: {manager.total_votes()}"

        #determines winner
        max_votes = max(manager.votes.values())
        winners = [name for name, count in manager.votes.items() if count == max_votes]

        if len(winners) == 1:
            text += f"\nWinner: {winners[0]}"
        else:
            text += f"\nTie: {', '.join(winners)}"

        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)
