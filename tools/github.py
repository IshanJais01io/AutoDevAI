import os
import subprocess


class GitHubTool:


    def clone_repository(self, url):

        repo_name = url.split("/")[-1]

        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]


        path = os.path.join(
            "workspace",
            repo_name
        )


        os.makedirs(
            "workspace",
            exist_ok=True
        )


        if os.path.exists(path):

            print("Repository already exists")

            return path



        subprocess.run(
            [
                "git",
                "clone",
                url,
                path
            ]
        )


        return path