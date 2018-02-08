import requests
from datetime import date, timedelta


def get_trending_repositories(top_size=20, days=7):
    url = 'https://api.github.com/search/repositories'
    due_date = date.today() - timedelta(days=days)
    payload = {
        'q': 'created:>{}'.format(due_date),
        'sort': 'star',
        'order': 'desc',
        'page': '1',
        'per_page': top_size,
    }
    repos_list = requests.get(url, params=payload).json()['items']
    return repos_list


def get_open_issues_list(repo):
    url = 'https://api.github.com/repos/{}/issues'.format(repo['full_name'])
    issues_list = requests.get(url).json()
    issues_url_list = [issue['html_url'] for issue in issues_list]
    return issues_url_list


def output_results(index, repo, issues_url_list):
    print('\n№{} repository: {}, owner: {}'.
          format(index, repo['name'], repo['owner']['login']))
    print('Open issues amount: {}'.format(len(issues_url_list)))
    if len(issues_url_list):
        for url in issues_url_list:
            print(url)


if __name__ == '__main__':
    repos_list = get_trending_repositories()
    print('Top-20 repositories for last 7 days on {}'.format(date.today()))
    for index, repo in enumerate(repos_list, 1):
        issues_url_list = get_open_issues_list(repo)
        output_results(index, repo, issues_url_list)
