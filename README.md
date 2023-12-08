# DS5111_SW_Skills_II
SW Skills Labs I, II, III


Part II questions:

What did you have to do to get make to work?

One of the challenges when working with both makefiles and python files is that makefiles need diligent attention given to indentation which must be tabbed (not using spaces), however, the python files must use 4 spaces as indentation. This needs to be changed within the jupyter lab UI each time you switch. 

Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)

In part 1 of the lab, when running the virtual environment within the makefile, adding source did not work, rather you had to change it to . to get the makefile to run.

Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. 

In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ;

The command on one line runs it sequentially.

As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?

If there wa a file called run it would cause a conflict and return an error. You would have to fix the naming convetion or incldue error handling.

The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?

It appends the current directory to the sys.path


Extra Credit:


•	1 point: Your .gitignore has 'env/', and also a callout to ignore the compiled python files, the ones in __pycache__ folders. What is the meaning of the **/* ?

It represents all the files and directories in any subdirectory of the repository.

•	1 point: do a pip list or pip freeze and call out versions of the pytest and pylint packages in your requirements.txt. Include them in your requirements.txt, and for the extra credit, just add a note reminding me you included them.

We had to update packages to get the pylint to work so the package of python was updated within the GitHub UI itself.

•	1 points: In the sample code from the book, why does the line if __name__=="__main__": allow the script to run if called directly, but not otherwise? What's going on there?

It checks if the python script is being run directly by the interpretor rather than being imported as a module into another script.

•	1 point: If you add two print statements, (or any statements for that matter), one above and one below the if __name__... line, what would happen when I do an import of the file? What happens when I call the file directly with python <filename>. Most importantly, why?.

If the code is before or after the block it will execute during import as it's a part of the code flow.
