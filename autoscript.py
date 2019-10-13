if __name__ == "__main__":
    repo_path = os.getenv('GIT_REPO_PATH')
   
    repo = Repo(repo_path)
   
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
            pass
    else:
        
        for commit, lines in repo.blame('HEAD', filepath):
    if tlc <= ln < (tlc + len(lines)):
         print(commit)
    tlc += len(lines)
