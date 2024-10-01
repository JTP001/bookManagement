# bookManagement
A simple book management system using Django. This was done for an internship application project challenge to the specifications required.

How to run this project:

There are two setup files, setup.ps1 and setup.sh. 
- If you are in a linux environment, do 'bash setup.sh' in the project directory. You may need to do 'chmod -x setup.sh' first if it says you don't have permissions to execute the file. Note that this will check if your system has python3 and python3-venv installed and install them if needed, as they are required.
- If you want to do it through Windows Powershell, do './setup.ps1' in the project directory. 

In both cases, a virtual environment will be created where the related packages will be installed, and then the project will be run.
Once run, the Django development server will be started locally on your machine. You will see the dialogue below after running the Django server with the setup file:

![Screenshot 2024-10-01 153845](https://github.com/user-attachments/assets/e0bd53d1-564c-413b-8da1-6000c4786f34)

Command click or copy-paste the underlined line into a browser to see your local development server with the program running on it, and you're done.
