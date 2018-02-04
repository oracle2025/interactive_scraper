# Interactive Scraper

for python

This is an approach to build a scraping tool, that allows interactive
exploration.

I had the problem that every now and then I want to automate some access to a
website, but I do it to seldom to actually remember an API like beautifulsoup.

Therefore I decided to use the autosuggest functionality of python to build a
scraping api that exposes the found objects as functions, and can therefore be
easily discovered in the python repl.

## Activiting tab completion in python

[source](https://stackoverflow.com/a/246779)

Create a file .pythonrc

  \# ~/.pythonrc
  \# enable syntax completion
  try:
        import readline
  except ImportError:
        print("Module readline not available.")
  else:
        import rlcompleter
        readline.parse_and_bind("tab: complete")

then in your .bashrc file, add

  export PYTHONSTARTUP=~/.pythonrc

## Requirements

  pip3 install beautifulsoup4
  pip3 install requests
  pip3 install MechanicalSoup
