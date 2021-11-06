# scmcdroot

The commands in this project Search upwards in the directory tree until they find an SCM directory or until they reach the root directory.

## scmcdroot - bash script 
Change to the SCM root directory of a directory under version control.  That is the directory containg the .git, .svn, .bzr, or .p4 directory

*Usage:*

. scmcdroot

To run the scmcdroot shell script, use '.' (dot), then ' ' (space), then "scmcdroot". 

*Note:*

You must "source" the script so that it runs in the current shell in order for the directory change to persist when the command ends.  If you don't source the script in the current shell, the system will start a new shell and run the script in that shell.  The directory will be changed in the new shell, but the directory in your current shell will not be changed.  When the new shell finishes running the script, you will be in your original shell, still in the directory you were in when you ran the script.

## scmwd - shell script
Print the scm working directory, ie. the directory containing the .git, .svn, .bzr, or .p4 directory.

You can change to that directory by executing the following command:

```
cd `scmwd` 
```

## scmwd.py - Python version of the above shell script.
Print the scm working directory, ie. the directory containing the .git, .svn, .bzr, or .p4 directory.

You can change to that directory by executing the following command:

```
cd `python scmwd` 
```
