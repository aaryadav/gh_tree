import os
import argparse
from dotenv import load_dotenv
from utils.gh import get_gh_tree

def main(username, repository):
    load_dotenv()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN not found in environment variables. Please set it in a .env file or as an environment variable.")
    
    try:
        tree = get_gh_tree(username, repository, token)
        print(tree)
    except Exception as e:
        print(f"Error occurred while fetching the GitHub tree: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch GitHub repository tree")
    parser.add_argument("-p", "--path", help="GitHub username and repository in the format 'username/repo'", type=str)
    args = parser.parse_args()

    path = args.path

    if not path:
        path = input("Please enter the GitHub username and repository in the format 'username/repo': ")

    username, repository = path.split('/')

    main(username, repository)