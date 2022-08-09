# Description
This is the repository containing all the assessments you must take to show your python coding proficiency. Each folder contains an assessment, and you must read the `readme.md` to discover what is the assessment is about precisely and implement your solution in the `file.py` by only filling the functions left empty for that purpose.

# Setup
Install the required packages to be able to run the evaluation locally.

You need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: python_coding_assessments> ...`  follow the steps below:

- Windows:
        
        python3 -m venv venv; venv\Scripts\activate; python -m pip install --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install --upgrade pip; python -m pip install -qr requirements.txt  
<!-- 
```command
python -m pip install -qr requirements.txt
``` -->


# Evaluation
This evaluation will be automatically grade, so please follow the instructions carefully. 

You can run this command bellow being at the root of the repository to be sure your solutions are the good ones before to push your solutions.
```command
python -m pytest -v
```

```command
python -m pytest -v exercise_name/tests
```

**NB**: Do not modify the content of any folder named `tests`, otherwise your local checking will not reflect the advanced tests that will be run when you will push your solutions.

# MCQ Test
Here is the link to access the MCQ test to take before to complete the whole assessment. This test is restricted to Azubi learners: [Click Here!](https://forms.office.com/r/ZHD623QXcs)

# Resources
1. [Documentation format](https://numpydoc.readthedocs.io/en/latest/format.html)
1. [Documenting python code](https://realpython.com/documenting-python-code/)