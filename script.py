import os
from dotenv import load_dotenv
import requests

load_dotenv()

def create_github_issue(repo_owner, repo_name, title, body, token):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    headers = {'Authorization': f'token {token}'}
    data = {'title': title, 'body': body}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f'Issue "{title}" created successfully!')
    else:
        print(f'Failed to create issue. Status code: {response.status_code}, Response: {response.text}')


repo_owner = os.getenv('REPO_OWNER')
repo_name = os.getenv('REPO_NAME')
issue_title = os.getenv('ISSUE_TITLE')
issue_body = os.getenv('ISSUE_BODY')
github_token = os.getenv('GITHUB_TOKEN')

create_github_issue(repo_owner, repo_name, issue_title, issue_body, github_token)