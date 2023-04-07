# Selenium-WebdriverManager-Python
Selenium scripts implementing unittest framework with webdriver manager class in Python for https://glycam.org/ for cross broswer testing - chrome and firefox. 

# About Selenium - Web driver
- An Automated testing tool for web devolopement
- Version in use selenium==4.1.3
- You can directly execute main.py with python3 after cloning the reporsitory if you already have the necessary installations
- sel_test1 is just a mock created to test some of the functionalities offered by selenium

# Installation of selenium web driver for Ubantu | Python 
1. Please make sure your system already has pip3, Python3 installed. Selenium is JAVA based, so you will also need JRE 1.6 or abover installed.(use following to check "pip3 --version", "python3 --version",  "java" or "java --version").

2. Use "pip install selenium" to install python bindings for selenium. In case you run into issues try using command "sudo pip3 -U install selenium"

3. Use "pip3 freeze" and check if you can find selenium with version 4.1.3 or the latest one, in the list. If not use "selenium==4.1.3" to set it, and check again using "pip3 freeze"

# Installation of webdriver manager for python
[Link to the tutorial](https://pypi.org/project/webdriver-manager/)

# CB Unit Test
This is an updated selenium test which uses selenium webdriver to check the carbohydrate builder utility on each step in the testing environment. 

The test uses 2 sequences to check cb utility - 1) "DManpa1-OH" & 2) "DManpa1-6DManpa1-6DManpa1-OH"
The smaller sequence skips the cb/options page and directly leads to the downloads page while the second sequence follows each step of the cb utility. 

Note - 
1. Please make sure you have installed the prerequisites as per - docs/selenium-installation.md
2. This test incorporates unittest framework, please use the following resources to learn about the same.
    Useful links
    - [techbeamers.com/selenium-python-test-suite-unittest](https://www.techbeamers.com/selenium-python-test-suite-unittest/#h1)
    - [youtube](https://www.youtube.com/watch?v=9_5Wqgni_Xw)
    Official docs
    - [selenium/docs](https://www.selenium.dev/selenium/docs/api/py/index.html)
    - [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/installation.html)

# Execution instructions
1. To run the test, make sure you have used ```bash Start-All-DevEnv.bash```
2. Move to current directory ```cd Django/glycam-django/glycamweb/cb/selenium_tests/cb_unit_test```
3. Use command ```python3 main.py <<choice_of_browser>>``` You can pass either chrome or firefox as an argument to the test

# Testing features 

1. Provides cross browser support. Currently works with chrome and firefox

2. The selenium test uses V_2/Proxy/env.txt to capture the current IP address using readIp() method, this is specific to development environment.If you are not using the environment you dont need this method. 

3. Uses build via text option to build the two said sequences

4. Each method in main.py that starts with "test" will be executed as separate test

5. On cb/options page, the selenium test will click on all the available rotamer options to ensure the functionality and build the entire sequence

6. On cb/options page, the selenium test will also check against the threshold structure count which is 64. If it goes beyond 64 the test will pass without building the entire sequence since this is the expected behavior of website

7. The test checks for availability of all the buttons labeled as "All conformer files" on cb/downloads page before checking the availability of "Download all" button

8. The test clicks on "Download all" button, and downloads the project.zip file in "Django/glycam-django/glycamweb/cb/selenium_tests/cb_unit_test/downloads" folder

9. It shows the size of downloaded file and deletes at the end of it's lifecycle

# Directions for update

When you need to write a new test, this will be defined in **main.py** Please note that the test method should start with the string "test" to be identified as test and executed. setUp and tearDown methods are executed before and after each test. You can use those methods for general setup and cleanup

In case you need to access a new eleement on the cb page for your test, you will need to define this element in **locator.py**. All the element selectors are defined in locator.py for easy maintainance

The **page.py** file defines the buisness logic of each test feature, and those methods are called in test methods of main.py. 

