import os
import requests
import subprocess
import sys

def get_repos(username, token):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}"
        response = requests.get(url, auth=(username, token))
        if response.status_code != 200:
            raise Exception(f"Error fetching repos: {response.status_code} {response.text}")
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def clone_or_update_repos(repos, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    for repo in repos:
        name = repo["name"]
        clone_url = repo["clone_url"]
        repo_path = os.path.join(dest_dir, name)

        if os.path.exists(repo_path):
            print(f"🔄 Repo '{name}' already exists. Pulling latest changes...")
            subprocess.run(["git", "pull"], cwd=repo_path)
        else:
            print(f"⬇️  Cloning '{name}'...")
            subprocess.run(["git", "clone", clone_url], cwd=dest_dir)

if __name__ == "__main__":
    GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    DEST_DIR = os.getenv("DEST_DIR", "./repos")

    if not GITHUB_USERNAME or not GITHUB_TOKEN:
        print("❌ Please set the environment variables GITHUB_USERNAME and GITHUB_TOKEN")
        sys.exit(1)

    print(f"Fetching repositories for user '{GITHUB_USERNAME}'...")
    repositories = get_repos(GITHUB_USERNAME, GITHUB_TOKEN)
    print(f"Found {len(repositories)} repositories.")
    print(f"Cloning or updating repositories into: {DEST_DIR}")
    clone_or_update_repos(repositories, DEST_DIR)
    print("✅ Done.")
