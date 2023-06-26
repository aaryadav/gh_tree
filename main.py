import os
from dotenv import load_dotenv
from utils.gh import get_gh_tree

load_dotenv()

username = "aaryadav"
repository = "waffle"
token = os.environ.get("GITHUB_TOKEN")
tree = get_gh_tree(username, repository, token)
print(tree)
