#!/usr/bin/python3
from rich.markdown import Markdown
from rich.console import Console
from rich.style import Style
from sys import argv,exit
getExc=lambda e:e.args[1] if len(e.args)>1 else str(e)
if len(argv)>1:
    pass
else:
    from os import path
    if not path.isfile('README.md'):
        exit('Pass .md filepath')
    else:
        argv.append('README.md')
try:
    with open(argv[1]) as fh:
        data=fh.read()
except FileNotFoundError as e:
    exit(getExc(e))
except Exception as e:
    exit(getExc(e))
Console().print(Markdown(data,))
