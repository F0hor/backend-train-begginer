import requests

url = 'https://api.github.com/users/'
url_sufix = '/events'


def parse(data):
    repo_data = dict()

    for d in reversed(data):
        repo = d['repo']['name']

        if repo not in repo_data.keys():
            repo_data[repo] = []

        repo_data[repo].append(d)
    
    for k in repo_data.keys():
        parse_repo(repo_data[k], k)

def parse_repo(data, repo):
    print(f'{repo} has {len(data)} events from user:')

    for d in data:
        event_type = d['type']
        
        match event_type:
            case 'CommitCommentEvent':
                parse_commit_comment(d)
            case 'CreateEvent':
                parse_create(d)
            case 'DeleteEvent':
                parse_delete(d)
            case 'DiscussionEvent':
                parse_discussion(d)
            case 'ForkEvent':
                parse_fork(d)
            case 'GollumEvent':
                parse_gollum(d)
            case 'IssueCommentEvent':
                parse_issue_comment(d)
            case 'IssuesEvent':
                parse_issues(d)
            case 'MemberEvent':
                parse_member(d)
            case 'PublicEvent':
                parse_public(d)
            case 'PullRequestEvent':
                parse_pull_request(d)
            case 'PullRequestReviewEvent':
                parse_pull_review(d)
            case 'PullRequestReviewCommentEvent':
                parse_pull_comment(d)
            case 'PushEvent':
                parse_push(d)
            case 'ReleaseEvent':
                parse_release(d)
            case 'WatchEvent':
                parse_watch(d)

def parse_commit_comment(data):
    print(f'--User commented on a commit')

def parse_create(data):
    print(f'--User created {data['payload']['ref_type']}')

def parse_delete(data):
    print(f'--User deleted {data['payload']['ref_type']}')

def parse_discussion(data):
    print(f'--discussion (TBD)')

def parse_fork(data):
    print(f'--User forked a repo')

def parse_gollum(data):
    print(f'--gollum (TBD)')

def parse_issue_comment(data):
    print(f'--User')

def parse_issues(data):
    print(f'--')

def parse_member(data):
    print(f'--')

def parse_public(data):
    print(f'--')

def parse_pull_request(data):
    print(f'--')

def parse_pull_review(data):
    print(f'--')

def parse_pull_comment(data):
    print(f'--')

def parse_push(data):
    print(f'--')

def parse_release(data):
    print(f'--')

def parse_watch(data):
    print(f'--')


username = input()

response = requests.get(url + username + url_sufix)

if response.status_code == 200:
    data = response.json()
    parse(data)
else:
    print(f'Error: {response.status_code}')
