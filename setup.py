from distutils.core import setup

op={"py2exe": {"includes": ["sip"]}}

setup(windows=['main_QQuickView.py'] , options=op)

#python setup.py py2exe