import requests
import json

def get_contents(url, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        raise Exception(f"Error: {response.text}")

def get_tree(contents):
    dirs = []
    files = []

    for item in contents:
        if item["type"] == "dir":
            dirs.append(item["name"])
        else:
            files.append(item["name"])

    dirs.sort()
    files.sort()

    return dirs, files

def print_tree(tree, url, token, level=0):
    output = ""
    dirs, files = tree

    for d in dirs:
        output += "│   " * level + "├── " + d + "\n"
        # print(ou)
        subdir_url = f"{url}/{d}"
        subdir_contents = get_contents(subdir_url, token)
        subdir_tree = get_tree(subdir_contents)
        # print(subdir_tree)
        output += print_tree(subdir_tree, url, token, level + 1)

    for f in files:
        output += "│   " * level + "├── " + f + "\n"

    return output

def get_gh_tree(username, repository, token):
    url = f"https://api.github.com/repos/{username}/{repository}/contents"
    contents = get_contents(url, token)
    tree = get_tree(contents)
    output = ".\n" + print_tree(tree, url, token)
    output += f"\n{len(tree[0])} directories, {len(tree[1])} files"
    return output