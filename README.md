# Github Trends

The script finds out Top-20 the most starred repositories on Github for last week, count amount of the open issues 
for each and outputs them out.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python3 github_trending.py
```

Note, the script needs package 'requests' to work. It would be installed by command:
```bash

$ pip3 instal -r requirements.txt
```

# Output example

```
Top-20 repositories for last 7 days on 2018-02-04

№1 repository: AutoSploit, owner: NullArray
Open issues amount: 12
https://github.com/NullArray/AutoSploit/pull/26
https://github.com/NullArray/AutoSploit/issues/25
https://github.com/NullArray/AutoSploit/issues/24
https://github.com/NullArray/AutoSploit/pull/23
https://github.com/NullArray/AutoSploit/pull/21
https://github.com/NullArray/AutoSploit/issues/20
https://github.com/NullArray/AutoSploit/issues/18
https://github.com/NullArray/AutoSploit/pull/10
https://github.com/NullArray/AutoSploit/issues/8
https://github.com/NullArray/AutoSploit/pull/6
https://github.com/NullArray/AutoSploit/issues/5
https://github.com/NullArray/AutoSploit/issues/4

№2 repository: minigo, owner: tensorflow
Open issues amount: 30
https://github.com/tensorflow/minigo/issues/51
https://github.com/tensorflow/minigo/issues/50
https://github.com/tensorflow/minigo/pull/48
https://github.com/tensorflow/minigo/issues/46
https://github.com/tensorflow/minigo/pull/45
https://github.com/tensorflow/minigo/issues/44
https://github.com/tensorflow/minigo/issues/43
https://github.com/tensorflow/minigo/issues/42
https://github.com/tensorflow/minigo/pull/41
https://github.com/tensorflow/minigo/pull/40
https://github.com/tensorflow/minigo/issues/37
https://github.com/tensorflow/minigo/issues/36
https://github.com/tensorflow/minigo/issues/35
https://github.com/tensorflow/minigo/pull/27
https://github.com/tensorflow/minigo/issues/26
https://github.com/tensorflow/minigo/issues/25
https://github.com/tensorflow/minigo/issues/24
https://github.com/tensorflow/minigo/issues/20
https://github.com/tensorflow/minigo/issues/15
https://github.com/tensorflow/minigo/issues/14
https://github.com/tensorflow/minigo/issues/13
https://github.com/tensorflow/minigo/issues/12
https://github.com/tensorflow/minigo/issues/11
https://github.com/tensorflow/minigo/issues/10
https://github.com/tensorflow/minigo/issues/9
https://github.com/tensorflow/minigo/issues/8
https://github.com/tensorflow/minigo/issues/7
https://github.com/tensorflow/minigo/issues/6
https://github.com/tensorflow/minigo/issues/5
https://github.com/tensorflow/minigo/issues/4
...
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
