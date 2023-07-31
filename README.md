1. Automated Playback of Amazon MiniTV Series - “Farzi Mushaira”

2. Description:
      Welcome to this project.! This is an automated test for the Amazon MiniTV web series. This project automates the playback of a web series from Amazon mini tv. In this project, the test automates the playback of the first episode from each season of "Farzi Mushaira Web Series" with the Selenium pytest Hybrid framework. This framework verifies the status of a video player i.e. the video is currently playing or paused, the duration of the video, and takes screenshots of the video and generates the allure reports.

```bash
Note: This project requires a stable internet connection to run smoothly. 
If you get any timeout exception in the console just check the internet connection and try again.
```

3. What this project does:
	- Opening Amazon MiniTV
	- Opens the Chrome browser.
	- Navigates to the Amazon MiniTV website    (URL:https://www.amazon.in/minitv).  
	- Finding and Selecting a Series
	- On the Amazon MiniTV homepage, locates a web series named “Farzi Mushaira”
	- Clicks on the series and opens the series detail page.
	- Finds out the seasons for the web series.
	- Click on each season option and play the first episode from each season.
	- Wait for the episode to play.
	- Once the video plays for a specific duration take a screenshot of the video and make assertions
	- Closes the video after successful play and navigates to another episode
	- Play an episode from another season and repeats points 5-7.
	- After successful completion of the test, it generates the pytest basic report in the project directory as report.html indicating the status of each episode's playback (e.g., 	  passed or failed).  (Run command as pytest --html=report.html
	- It can also generate allure reports if we run the command-   pytest --allurdir="./Reports" (Node JS should be installed to run allure reports)

4. How to Install and Run the Project:

	Pre-requisites for the project:

	Python 
	- Here you can download and install Python - https://www.python.org/downloads/ 
	- or Just Click Here.

	Pycharm IDE
	- From here you can download and install Pycharm IDE - https://www.jetbrains.com/pycharm/download
	- Or Just Click Here.
 	Node JS
        - From here you can download and install Pycharm IDE - 
  	  https://nodejs.org/en/download      
	- Or Just Click Here.

	Pytest  
	- After installing Python and Pycharm open the Python installation directory
	- Navigate to the Python/Scripts folder and add this path to the environment
  	  variable of the path in the system.   
	- Open the Command line tool or CMD and enter the below command.
	- pip install pytest


	Selenium
	- Open the cmd and type below command
	- pip install selenium
	- Allure pytest 
	- Open the cmd and type below command
	- pip install allure-pytest

	Note: Require basic knowledge of
	- Manual and Automation testing concepts
	- Python
	- Selenium
	- Pytest
	- Allure Reports
	- Basic knowledge of web technology and web applications

5. Open and Run the project:

	- Clone the repository or Download the zip folder of the project
	- Unzip the project 
	- Open Pycharm IDE
	- From the top toolbar click on file->Open and open the project folder
	- From the bottom toolbar click on the Terminal option Or From the top toolbar go 
	  to
	  View->Tool Windows->Terminal
	- Run the below command in the terminal
```bash 
	pytest -rA 
```
Or to generate simple report  or Allure report run

```bash
	pytest --html=report.html
	pytest --allurdir="./Reports"
```
	- You should be able to see the test running and video-related activity in the
	   browser.
	- To see the reports open the project folder in the directory 
	- Open the cmd at the project folder and run the below command
	- pytest --html=report.html to generate the basic report.
	- allure serve "./Reports" to generate an allure report.
	- You will be able to see all the reports.




6. How to Use the Project:

	- Open the project in Pycharm IDE

	 Folder structure:

	 configurations - This package contains all the configuration files for the project like the config.ini file.

	 Logs - This folder contains the log file which is generated after the test execution.

	 pages- This package contains all the pages for which the test scenario is applied.

	 Reports - This folder contains all the reports generated from allure reports.

	 screenshots- This folder contains all the screenshots captured to verify the videos are playing.

	 tests - This package contains all test methods which are used in the project.
   
	 utilities - This folder contains all the reusable methods to optimize the code.

 To Run the Project:

		- Open the project In Pycharm IDE
		- Open the terminal and hit the below command
		- pytest to run without reports Or pytest --alluredir = "./Reports" to generate the reports.
		- To get descriptional logs run pytest -rA command

7. After successful completion of the Test:
	- You will be able to see the console logs regarding the videos
	- All assertions will be invoked
	- Screenshots of videos will be captured and will be stored in the screenshots folder along with the season and episode name of the video

8. Congrats.! You are Ready to use the project. Happy Testing.


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Deployment

To deploy this project run


	- Clone the repository or Download the zip folder of the project
	- Unzip the project 
	- Open Pycharm IDE
	- From the top toolbar click on file->Open and open the project folder
	- From the bottom toolbar click on the Terminal option Or From the top toolbar go 
	  to
	  View->Tool Windows->Terminal
	- Run the below command in the terminal
    
```bash
    pytest --html=report.html
    Or
	pytest pytest --allurdir="./Reports"
```
	- You should be able to see the test running and video-related activity in the
	   browser.
	- To see the reports open the project folder in the directory 
	- Open the cmd at the project folder and run the below command
	- pytest --html=report.html to generate the basic report.
	- allure serve "./Reports" to generate an allure report.
	- You will be able to see all the reports.




## Documentation

[Documentation](https://linktodocumentation)


## Demo

Insert gif or link to demo


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

