#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rob/Documents/_CSCI499/USRP-dev-Sp19/gr-CS499/python
export PATH=/home/rob/Documents/_CSCI499/USRP-dev-Sp19/gr-CS499/build/python:$PATH
export LD_LIBRARY_PATH=/home/rob/Documents/_CSCI499/USRP-dev-Sp19/gr-CS499/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/rob/Documents/_CSCI499/USRP-dev-Sp19/gr-CS499/build/swig:$PYTHONPATH
/usr/bin/python2 /home/rob/Documents/_CSCI499/USRP-dev-Sp19/gr-CS499/python/qa_numbers.py 
