from distutils.core import setup
import py2exe

op={"py2exe": {"includes": ["sip"]}}

setup(windows=['main.py'] , options=op)

#python setup.py py2exe