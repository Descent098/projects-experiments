# Useful Example

This folder puts together what I learned in the `/basics` and `/structs` combined with a bit more structure to keep things clean. This demo will be using go to do some web scraping, then dumping the results to python, while keeping the python API simple to use.

## Running

You should be able to run by just running `testing.py`, if you have your go and c compiler setup it will compile the lib and run it for you, or if it fails it will give you the command to run.

## Improvements

I made some improvements compared to `/structs`:

1. Since the types are converted to python objects when they come back, I immediately free the variables after I get them back
2. With potential problems popping up over the lib being compiled or not, I added an automatic check to `scraping/__init__.py` that will try to build if it's not present
