# MLOps Demo — Pandas Mini-Project  

This repository is part of my Ironhack bootcamp work, where I explored Pandas fundamentals while structuring the project in an **MLOps-style workflow**.  
It includes lab exercises, the `Admission_Predict.csv` dataset, and supporting Python scripts.  

## Roles (per lab)  
- **Developer:** Affiwhizz  
- **Gatekeeper/Reviewer:** Lukman Kayode Sadiq  

## Quickstart  

1. Clone the repo  
   ```bash
   git clone https://github.com/Affiwhizz/mlops-demo.git
   cd mlops-demo

**Install dependencies**
pip install -r requirements.txt

**Run the script**
python src/ml_ops.py


**Features**
- Creates a Pandas Series and demonstrates indexing.
- Builds a small DataFrame and performs column/row operations.
- Loads data/Admission_Predict.csv and prints simple stats/filters.

**Lab Workflow (Developer → Gatekeeper)**
Developer (Affiwhizz):
- Set up repo, virtual environment, and requirements file
- Pushed initial commit to remote
- Created a feature branch with small change
- Opened a Pull Request

**Gatekeeper (Lukman Sadiq):**
- Reviewed the PR
- Pulled branch locally, ran the code with venv + requirements
- Confirmed it worked and merged to main

**Sample Output****
Here’s an example run of the script:
<img width="948" height="797" alt="Screenshot 2025-09-08 at 17 33 58" src="https://github.com/user-attachments/assets/90030d6b-ad66-4bef-ba4a-900ab1863b0c" />

**Future Work**
- Expand data analysis with more complex Pandas operations
- Add unit tests to validate data transformations
- Integrate GitHub Actions for automated testing
- Explore packaging this project as a Python module

**Notes**
Python 3.10+ recommended
Dataset is for teaching/demo only

This repo reflects my learning journey with Pandas and Git/GitHub workflows. Feel free to fork or suggest improvements.