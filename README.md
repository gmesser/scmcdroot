scmcdroot
=========

Change to the SCM root directory of a directory under version control.

Search upwards in the directory tree until an SCM dir is found or the root
directory is reached.
If found, leave the current directory where the SCM directory was found.
If not found, return to the starting directory.

Usage: . scmcdroot

Note: This is a shell script which runs under /bin/sh. 
The command is '.' (dot), then ' ' (space), then "scmcdroot". 
You must source the script in the current shell or else the system will 
run the script in a new shell, where the directory will be changed, but
the directory in your current shell will not be changed.  When the new
shell finishes running the script and ends, you will be in your original
shell, still in the directory you were in when you ran the script.

