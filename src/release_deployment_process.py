```python
import os
from git import Repo

class ReleaseDeploymentProcess:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = Repo(self.repo_path)

    def versioning(self, version):
        # Update version in a dedicated version file
        with open(os.path.join(self.repo_path, 'VERSION'), 'w') as version_file:
            version_file.write(version)

        # Commit version file
        self.repo.git.add('VERSION')
        self.repo.git.commit('-m', f'Update version to {version}')

    def testing(self):
        # Run tests
        os.system('pytest tests/')

    def ci_cd_pipeline(self):
        # Push changes to remote repository
        self.repo.git.push()

        # Trigger CI/CD pipeline (assuming a pipeline is set up on the remote repository)
        print("CI/CD pipeline triggered")

    def release_process(self, version):
        self.versioning(version)
        self.testing()
        self.ci_cd_pipeline()

    def deployment_process(self):
        # Assuming a deployment process is set up on the remote repository
        print("Deployment process started")

if __name__ == "__main__":
    rdp = ReleaseDeploymentProcess('/path/to/repo')
    rdp.release_process('1.0.0')
    rdp.deployment_process()
```