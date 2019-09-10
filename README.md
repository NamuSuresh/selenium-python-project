# selenium-python-project
This work is to show a hint of my experience with automation using selenium web driver and python in pycharm

## installation
1. PyCharm 2019.1.3, build PC-191.7479.30. Copyright JetBrains s.r.o., (c) 2000-2019
2. Python version 3.6
3. Chrome driver:Downloaded it and sent the path to scripts
4. In Project interpreter 
  - Pip 19.0.3
  - Selenium 3.141.0
  - setuptools 40.8.0
  - Virtualenv 16.7.4
 
 ## apply Page-Object-Pattern
 1. Build a base page, which will be inherited by all the other pages. Here we will keep all the common code specific to selenium.
 2. Implemented the Homepage, Registration_Page, Login_Page and Search_Page.
   <img src="https://github.com/NamuSuresh/selenium-python-project/blob/master/images/TestProject.png" width="256" height="256" title="Github Logo">  
 3. Created a test template page -> inherited by all the tests. It’s like a blueprint of a test.
 4. Created TestsScripts for Homepage, Registration_Page, Login_Page and Search_Page.
 5. Created Test Runner(A test runner is the library or tool that picks up an assembly (or a source code directory) that contains unit tests, and a bunch of settings, and then executes them and writes the test results to the console or log files.) run tests sequentially using simple TextTestRunner
 
 
