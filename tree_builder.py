#!/usr/bin/env python3
"""First module"""


import requests
import json

user = 'LuisPatino92'
token = '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'

def get_sha(default_branch, branches_url):
    raw_info = json.loads(requests.get(branches_url, auth=(user, token)).text)
    for element in raw_info:
        if element["name"] == default_branch:
            return element["commit"]["sha"]

def get_files(tree_url, sha):
    raw_info = json.loads(requests.get("{}/{}".format(tree_url, sha), auth=(user, token)).text)
    files = []
    for element in raw_info["tree"]:
        files += [element["path"]]
    return files

def get_tree(gitHubProfile):
    url = 'https://api.github.com/users/{}/repos'.format(gitHubProfile)
    raw_info = json.loads(requests.get(url, auth=(user, token)).text)

    student_repos = {}

    for repo in raw_info:
        student_repos[repo["name"]] = {}
        sha = get_sha(repo["default_branch"], repo["branches_url"].replace(f"{{/branch}}", ""))
        student_repos[repo["name"]]["files"] = get_files(repo["trees_url"].replace(f"{{/sha}}", ""), sha)

    return(student_repos)

if __name__ == '__main__':
    gitHubProfile = "LuisPatino92"
    #with open("{}.txt".format(gitHubProfile), 'w') as out_file:
    #    json.dump(get_tree(gitHubProfile), out_file, indent=4)
    with open("{}.txt".format(gitHubProfile), 'r') as out_file:
        my_dict = json.load(out_file)

    print(json.dumps(my_dict, indent=4))