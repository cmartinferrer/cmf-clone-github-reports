# 🧩 Clone All GitHub Repositories

This script allows you to automatically **clone all repositories** from your GitHub account using the GitHub API.

Ideal for:

- Backing up your repositories
- Syncing your work across machines
- Managing personal and private repos locally

---

## 📦 Requirements

- Python 3.6+
- `git` command-line tool
- GitHub [Personal Access Token](https://github.com/settings/tokens) 
- Python package: [`requests`](https://pypi.org/project/requests/)

---

## 🔐 Environment Variables

To keep your credentials secure, the script reads your GitHub username and token from environment variables.

### Required:

| Variable          | Description                             |
|------------------|-----------------------------------------|
| `GITHUB_USERNAME`| Your GitHub username                    |
| `GITHUB_TOKEN`   | Your GitHub personal access token       |

### Optional:

| Variable  | Description                                        | Default      |
|-----------|----------------------------------------------------|--------------|
| `DEST_DIR`| Directory to clone repos into                     | `./repos`    |

---

## 🚀 Usage

### 1. Clone this repo or download the script

```bash
git clone https://github.com/tu_usuario/clone-all-github-repos.git
cd clone-all-github-repos
```

### 2. Set environment variables
#### Linux / macOS
```bash
export GITHUB_USERNAME=your_username
export GITHUB_TOKEN=your_token
export DEST_DIR=./my_repos    # optional
```

#### Windows (CMD)
```bash
set GITHUB_USERNAME=your_username
set GITHUB_TOKEN=your_token
set DEST_DIR=.\my_repos
```

### 3. Install Python dependencies
❗ Note for Python 3.13+ users (like Homebrew Python on macOS):
Due to PEP 668, installing packages globally is restricted. Use the following command to install dependencies safely:

```bash
pip3 install --break-system-packages -r requirements.txt
```
This is safe if you're using Homebrew-installed Python.

### 4. Run the script
```bash
python clone_all_repos.py
```

## 📝 New behavior (second run and onwards)
If a repository already exists in the target directory, the script will pull the latest changes from GitHub (git pull).
If the repository doesn't exist, it will be cloned as usual (git clone).

## 💡 Example Output
```text
Fetching repositories for user 'johndoe'...
Found 12 repositories.
Cloning repo-one...
Cloning repo-two...
Skipping existing repo: repo-three
✅ Done.
```

## 🔒 Security Notes

Never commit your personal access token to version control.
Use environment variables or secret managers for production environments.
You can revoke tokens at any time from GitHub Developer Settings.


## 🧪 Test Your Token

To verify your token works:

```bash
curl -u your_username:your_token https://api.github.com/user/repos
```

## 📄 License

MIT License © [cmartinferrer](https://github.com/cmartinferrer/)
