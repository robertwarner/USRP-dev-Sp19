#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rob/gr-howto/python
export PATH=/home/rob/gr-howto/build/python:$PATH
export LD_LIBRARY_PATH=/home/rob/gr-howto/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/rob/gr-howto/build/swig:$PYTHONPATH
/usr/bin/python2 /home/rob/gr-howto/python/qa_square_ff.py 
