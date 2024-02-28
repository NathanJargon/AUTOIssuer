import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

def create_github_issue_every_10_minutes(repo_owner, repo_name, title, body, token):
    while True:
        create_github_issue(repo_owner, repo_name, title, body, token)
        time.sleep(600 * 2)
        
def close_all_issues(repo_owner, repo_name, token):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    headers = {'Authorization': f'token {token}'}

    response = requests.get(url, headers=headers)
    issues = response.json()

    for issue in issues:
        issue_number = issue['number']
        close_url = f'{url}/{issue_number}'
        close_data = {'state': 'closed'}
        close_response = requests.patch(close_url, json=close_data, headers=headers)

        if close_response.status_code == 200:
            print(f'Issue "{issue_number}" closed successfully!')
        else:
            print(f'Failed to close issue "{issue_number}". Status code: {close_response.status_code}, Response: {close_response.text}')


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

for i in range(5):
    create_github_issue(repo_owner, repo_name, f'Issue {i+1}', f'Body of Issue {i+1}', github_token)
close_all_issues(repo_owner, repo_name, github_token)