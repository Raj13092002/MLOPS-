import os
from pathlib import Path #this librabry take care of the wrong path or worng slase(/,\)


list_of_files=[
    ".github/workflows/.gitkeep", #this is for workspace
    #src-- source code
    "src/__init__.py",#by this we a/c run the all the file without call them
    "src/components/__init__.py",#make the component folder and in this all the files are there
    "src/components/dara_ingestion.py",#make the data ingestion file
    "src/components/data_transformation.py",#make the transformation 
    "src/components/model_trainer.py",#make the trainer
    "src/components/model_evaluation.py",#make the model evaluation file
    "src/pipeline/__init__.py",#make the pipeline folder
    "src/pipeline/training_pipeline.py",#training folder of pipeline
    "src/pipeline/prediction_pipeline.py",#prediction folder of pipeline
    "src/utils/utils.py",#Python Utils is a collection of small Python functions and classes which make common patterns shorter and easier
    "src/utils/__init__.py",
    "src/logger/logging.py",# by this we log on them
    "src/exception/exception.py",# by this we handle the exceptions 
    "src/exception/__init__.py",
    "tests/unit/exception/__init__.py", #make the testing folder in this we have unit testing
    "tests/intergration/__init__.py", # make the intergration testing file in the test folder
    "init_setup.sh",# to setup the all the foder and files
    "requirements.txt",#in this all the requird package names are stored on it for run the files
    "requirements_dev.txt",# in this all the pacages names are stored for development 
    "setup.py",# to setup all the codes from the files
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"#make the files for experiments.
]

for filepath in list_of_files: #run the loop so that all the files are make on the githubs
    filepath=Path(filepath) #give the file path (.github/workflow/.gitkey)
    filedir,dilename=os.path.split(filepath) # split the directory and file name
    if filedir !="": #file directory is not empty
        os.makedirs(filedir,exist_ok=True) # make the directory od the name is filedir and exist is true means perments make the directory
        #logging.info(f"Creating directory:{filedir} for file:{filename}") # print the directory name and the file name
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass #create an empty file
    



