# stepik.selenium.python.autotest.final_project
Final project for selenium-python autotest course: https://stepik.org/lesson/201964/step/15?unit=176022

# Environment setup
- Install Python 3.8 on your computer
- Install text editor, preferably PyCharm IDE
- Install version control system - git: https://git-scm.com/downloads
- Make sure that you have Chrome installed and the `chromedriver` in `PATH` witch matches your Chrome version download ChromeDriver set the `PATH` too
- Make sure that you have Firefox installed and the geckodriver in PATH witch matches your Firefox version download GeckoDriver set the PATH too

# To start with the project:
- Create a virtual environment for the project: 
`cd project_folder`
`virtualenv venv`
- Activate your virtual environment: 
`cd project_folder`
`cd venv\Scripts\activate.bat`
- Install required dependencies: 
`cd project_folder`
`pip install -r requirements.txt`
- Copy `chomedriver.exe` and `geckodriver.exe` files from your computer to the main directory of the project

# Execute tests and get the report:
- Run the tests with Chrome using the command: 
`pytest -v --tb=line` 
or `pytest -v --tb=line --browser_name=chrome`. 
- Run the tests with Firefox using the command:
`pytest -v --tb=line --browser_name=firefox`
- You will get test results report in the terminal after running the tests 
