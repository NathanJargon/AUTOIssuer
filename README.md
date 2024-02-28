# AUTOIssuer :octocat:

This repository contains a Python script that automates the process of creating and closing issues in a GitHub repository using the GitHub API.                                                       

## :gear: Setup & Usage

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Installation

1. Clone this repository and navigate into it:

```bash
git clone https://github.com/your_username/AUTOIssuer.git
cd AUTOIssuer
```
2. Install the required Python packages:

```bash
pip install python-dotenv requests
```
    
### Configuration

Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
REPO_OWNER=your_username
REPO_NAME=your_repository
ISSUE_TITLE=Your Issue Title
ISSUE_BODY=Description of your issue
GITHUB_TOKEN=your_personal_access_token
```

### Running the Script

Execute the script using Python:

```bash
python script.py
```

## :warning: Warning

- The `close_all_issues` function will close all open issues in the specified repository. Use this function with caution, as closing issues cannot be undone through the API.

- Creating a large number of issues in a short period of time might be considered abuse of the GitHub API and could potentially lead to your account being flagged or rate-limited. Use the script responsibly and only create issues as needed.

## :handshake: Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/NathanJargon/AUTOIssuer/issues).