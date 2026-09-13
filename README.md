Step1. make a git repo and a github repo for it
Step2. make a virtual environment and install the dependencies (conda create -n cicd-demo python=3.11 -y and conda activate cicd-demo)
Step3. make requirements.txt file and add the dependencies (pip install fastapi uvicorn pytest httpx flake8)
Step4. make a main.py file and add the fastapi code
# Test the application locally
Step5: uvicorn main:app --reload
Step6: open http://127.0.0.1:8000/ in the browser
Step7: test the application (http://127.0.0.1:8000/add?a=5&b=10)