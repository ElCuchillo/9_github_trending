import requests
from datetime import date, timedelta


def get_trending_repositories(top_size, age):
    url = 'https://api.github.com/search/repositories?' \
          'q=created:>{}&sort=stars&order=desc'.\
          format(str(date.today() - timedelta(days=age)))
    repos_list = requests.get(url).json()['items'][:top_size]
    return repos_list


def get_open_issues_list(repo):
    url = 'https://api.github.com/repos/{}/issues'.format(repo['full_name'])
    issues_list = requests.get(url).json()
    issues_url_list = [issue['html_url'] for issue in issues_list]
    return issues_url_list


def output_issues_info(repos_list):
    for n, repo in enumerate(repos_list):
        print('\n№{} repository: {}, owner: {}'.
              format(n+1, repo['name'], repo['owner']['login']))
        issues_url_list = get_open_issues_list(repo)
        print('Open issues amount: {}'.format(len(issues_url_list)))
        if len(issues_url_list):
            for url in issues_url_list:
               print(url)


if __name__ == '__main__':
    top_size = 20
    age = 7
    repos_list = get_trending_repositories(top_size, age)
    print('Top-{} repositories for last {} days on {}'.
          format(top_size, age, date.today()))
    output_issues_info(repos_list)
