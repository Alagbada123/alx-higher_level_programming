#!/usr/bin/env python3
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        commits = response.json()
        
        for commit in commits[:10]:  # Get the 10 most recent commits
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            if sha and author:
                print(f"{sha}: {author}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
