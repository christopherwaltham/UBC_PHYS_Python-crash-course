# 0. Setting Up the Tools

## Installing Anaconda
Anaconda is a package manager (program that helps you install all the things you need, and that keeps it organised) which is made for Python. To install Anaconda, do the following:

- Download the "Python 3.7 version" installer suitable for your operating system from https://www.anaconda.com/download/
- Run the installer.
- You will get a prompt to install Visual Studio Code. We do not need this text editor for this course, so you do not need to download it.

## Setting up a virtual environment
Different projects might need to use different versions of Python. We will, therefore, set up "virtual environments" every time we want to run Python code, to make sure we are interfacing with the packages and installations we want.
- Launch Anaconda Navigator (you will find Anaconda in launchpad on Mac or your start menu on Windows).
- Go to the "Environments" tab on the left-hand side of the screen.
- Click the "Create" button at the bottom of the screen. The dialogue seen in this figure will appear:
![](Images/Anaconda1.png)
- Give the environment a name of your choosing (for example "PHYS_TUT").
- Select the check-box for Python and select 2.7 from the dropdown (yes, 2.7, not 3.7, even though you downloaded the 3.7 release). This is the version of Python we are going to use.
- Ensure R is unchecked. R is a comletely separate programming language focussed on statistics applications.
- Hit "Create".

You have now made your own environment. It may appear below your "base (root)" environment which is the global environment on your computer.

We can now install the packages we need in our newly made environment. Do as follows:
- Ensure the environment we just created is active. If not, simply click on it to activate it. Changing environments can take some seconds, so be patient.
![](Images/Anaconda2.png)
- Select "Not installed" from the dropdown and search for "pyserial". When it appears, select the checkbox for the package and hit "Apply".
![](Images/Anaconda3.png)
- Select "Apply" in the dialogue and wait until the package is installed.
- Repeat these steps to install another package called "numpy". It has some dependencies that will be automatically installed.

## Getting started with Spyder
Spyder is a scientific Python development environment that makes it easy to write and run Python code. You can install it from within Anaconda as follows:
- Go to the "Home" tab on the upper left side of the Anaconda window.
- Find Spyder and click "Install". Wait until the installation is completed.

To start working with Spyder, do the following:
- Ensure the "Applications on" dropdown on the top of the creen is set to the environment "PHYS_TUT" that we just created.
- Hit "Launch" on Spyder.
- You are now greeted with the Spyder interface. It consists of three parts:
  - Code editor: where you write your Python code
  - Directory: where you store and access your files
  - Console: where you run and view the output from your code
![](Images/Spyder1.png)
- After you have written some code you want to run, click the green play button at the top of the screen.
- Set the directory path (circled in the picture above) to where you want your code to be saved.

You have now got all you need to start writing Python! Go to the module next module to continue.

Next: [Learning Python](/1.%20Learning%20Python/)
