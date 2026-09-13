Step1. make a git repo and a github repo for it
Step2. make a virtual environment and install the dependencies (conda create -n cicd-demo python=3.11 -y and conda activate cicd-demo)
Step3. make requirements.txt file and add the dependencies (pip install fastapi uvicorn pytest httpx flake8)
Step4. make a main.py file and add the fastapi code
# Test the application locally
Step5: uvicorn main:app --reload
Step6: open http://127.0.0.1:8000/ in the browser
Step7: test the application (http://127.0.0.1:8000/add?a=5&b=10)
# Testing the application with pytest and linter
Step8: make test_main.py file and add unit tests
Step9: run pytest to test endpoints
Step10: run flake8 . to check code style and formatting

# Setting up CI Pipeline
Step11: make the .github/workflows/ci.yml file
Step12: git add, commit, and push to main (triggers CI pipeline on GitHub)

# Feature Branch & Pull Request Workflow
Step13: create a new feature branch (git checkout -b feature/multiply)
Step14: add new endpoint in main.py and new test in test_main.py
Step15: test locally with pytest and flake8 .
Step16: push branch to github (git push -u origin feature/multiply)
Step17: open a Pull Request (PR) on GitHub
Step18: watch CI run automatically on the PR, then merge PR into main
Step19: update local main branch (git checkout main && git pull origin main)

# Continuous Delivery (CD) with Docker
Step20: make .dockerignore file to exclude unnecessary files
Step21: make Dockerfile to package the app into a container
Step22: add build-and-push job to ci.yml with needs: [test]
Step23: push to main and watch GitHub Actions build and publish the Docker container to GitHub Packages (ghcr.io)

