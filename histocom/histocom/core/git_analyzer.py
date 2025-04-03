import subprocess
from datetime import datetime, timedelta
from typing import List as Lt
from typing import Dict as Dt

class _CommitAnalyser:
    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path
    def get_commits(self, days_back: int = 30):
        since_date = (datetime.now()-timedelta(days=days_back)).isoformat()

        result = subprocess.run(
            ["git", "-C", self.repo_path, "log", 
             f"--since={since_date}",
             "--pretty=format:%h|%aI|%an|%s"],
            capture_output=True,
            text=True,
            check=True
        )
        commits = []
        for line in result.stdout.splitlines():
            parts = line.split("|")
            commits.append({
                "sha" : parts[0],
                "date" : parts[1],
                "author" : parts[2],
                "message": parts[3]
            })

        return commits