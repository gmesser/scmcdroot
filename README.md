scmcdroot
=========

Change to the SCM root directory of a directory under version control.

Search upwards in the directory tree until an SCM dir is found or the root
directory is reached.
If found, leave the current directory where the SCM directory was found.
If not found, return to the starting directory.
