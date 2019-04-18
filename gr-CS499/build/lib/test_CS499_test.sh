#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/ty/Desktop/sdr/shared/USRP-dev-Sp19/gr-CS499/lib
export PATH=/home/ty/Desktop/sdr/shared/USRP-dev-Sp19/gr-CS499/build/lib:$PATH
export LD_LIBRARY_PATH=/home/ty/Desktop/sdr/shared/USRP-dev-Sp19/gr-CS499/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-CS499 
