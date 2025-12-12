import csv
from pathlib import Path
from typing import Dict, Set, Optional

# Disclosure: I used AI to help structure parts of this file.
# I reviewed and edited the code from AI to meet the assignment requirements.


class VoteManager:
    """Manage voting data: candidate counts and which voter IDs have voted.

    Data is stored in two CSV files in the application directory:
    - `votes.csv` contains candidate vote counts (candidate, votes)
    - `voters.csv` contains a list of voter IDs, one per line

    This class provides methods to register a vote while preventing
    duplicate voting by voter ID.
    """

    def __init__(self, data_dir: Optional[Path] = None) -> None:
        """Create a VoteManager and load any existing data.

        Args:
            data_dir: Optional path where CSV files are stored. Defaults
                      to current working directory.
        """
        if data_dir is None:
            data_dir = Path.cwd()
        self.data_dir = Path(data_dir)
        self.votes_file = self.data_dir / "votes.csv"
        self.voters_file = self.data_dir / "voters.csv"

        # default candidates
        self._votes: Dict[str, int] = {"Isabella": 0, "Genji": 0, "Hannah": 0}
        self._voters: Set[str] = set()

        self._load()

    def _load(self) -> None:
        """Load votes and voter IDs from disk, if present."""
        # load votes
        try:
            if self.votes_file.exists():
                with self.votes_file.open("r", newline="", encoding="utf-8") as fh:
                    reader = csv.reader(fh)
                    headers = next(reader, None)
                    for row in reader:
                        try:
                            name, count = row
                            self._votes[name] = int(count)
                        except Exception:
                            # if something fails, just continue
                            continue
        except Exception:
            # if loading fails, keep defaults
            pass

        # load voters
        try:
            if self.voters_file.exists():
                with self.voters_file.open("r", newline="", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row:
                            self._voters.add(row[0])
        except Exception:
            pass

    def save(self) -> None:
        """Persist vote counts and voter IDs to disk."""
        try:
            with self.votes_file.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(fh)
                writer.writerow(["candidate", "votes"])
                for name, count in self._votes.items():
                    writer.writerow([name, count])
        except Exception:
            # In a real app, we would log this
            pass

        try:
            with self.voters_file.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(fh)
                for voter_id in sorted(self._voters):
                    writer.writerow([voter_id])
        except Exception:
            pass

    def register_vote(self, voter_id: str, candidate: str) -> bool:
        """Register a vote for candidate from voter_id.

        Args:
            voter_id: Unique string identifying the voter so they  can't vote again.
            candidate: Candidate name to vote for.

        Returns:
            True if vote accepted and recorded; False if voter already voted.
        """
        voter_id = voter_id.strip()
        if not voter_id:
            raise ValueError("Voter ID must not be empty")

        if voter_id in self._voters:
            return False

        # makes sure the candidate exists
        if candidate not in self._votes:
            raise ValueError(f"Unknown candidate: {candidate}")

        self._voters.add(voter_id)
        self._votes[candidate] = self._votes.get(candidate, 0) + 1
        self.save()
        return True

    def get_votes(self) -> Dict[str, int]:
        """Return a copy of vote counts."""
        return dict(self._votes)

    def total_votes(self) -> int:
        """Return the total number of votes."""
        return sum(self._votes.values())

    def has_voted(self, voter_id: str) -> bool:
        """Return True if the given voter_id already voted."""
        return voter_id.strip() in self._voters

    def add_candidate(self, name: str) -> None:
        """Add a candidate to the ballot. If candidate exists, do nothing."""
        if name not in self._votes:
            self._votes[name] = 0
            self.save()

    def get_winner(self) -> Optional[str]:
        """Return the name of the winner or None if no votes yet.

        In case of a tie, returns the first in alphabetical order of winners.
        """
        if not self._votes:
            return None
        max_votes = max(self._votes.values())
        if max_votes == 0:
            return None
        winners = [n for n, c in self._votes.items() if c == max_votes]
        winners.sort()
        return winners[0]
