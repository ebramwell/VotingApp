from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from models.vote_manager import VoteManager

# Note: small portions of this file were assisted by AI during scaffolding.
# The developer reviewed and edited the code; results formatting kept simple
# for clarity for a beginner student.


class ResultsWindow(QWidget):
    """Window that displays vote results."""

    def __init__(self, manager: VoteManager) -> None:
        super().__init__()
        self.setWindowTitle("Voting Results")
        self.manager = manager

        layout = QVBoxLayout()

        # Build results text
        text_lines = []
        for name, count in sorted(self.manager.get_votes().items()):
            text_lines.append(f"{name}: {count} votes")

        total = self.manager.total_votes()
        text_lines.append("")
        text_lines.append(f"Total Votes: {total}")

        # Determine winner
        winner = self.manager.get_winner()
        if winner:
            text_lines.append(f"\nWinner: {winner}")
        else:
            text_lines.append("\nWinner: (no votes yet)")

        label = QLabel("\n".join(text_lines))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)
