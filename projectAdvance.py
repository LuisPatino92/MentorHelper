#!/usr/bin/python3

import sys
import requests
import json

key_t = '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'
usu = 'LuisPatino92'


def get_commits(user):

    repo = sys.argv[1].split('/')[0]
    path = sys.argv[1].split('/')[1]

    url = 'http://api.github.com/repos/{}/{}/commits?path={}'.format(user, repo, path)

    raw_info = json.loads(requests.get(url, auth=(usu, key_t)).text)

    return (len(raw_info))


with open('peers.txt', 'r') as student_list:

    stats = {}

    for line in student_list.readlines():
        st_name = line.split(',')[0]
        gitHub = line.split(',')[1][:-1]

        stats[st_name] = get_commits(gitHub)

    for element in stats:
        print("{:>29}  |  {}".format(element, stats[element]))
