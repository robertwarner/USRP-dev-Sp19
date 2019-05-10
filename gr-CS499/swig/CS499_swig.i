/* -*- c++ -*- */

#define CS499_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "CS499_swig_doc.i"

%{
#include "CS499/get_time.h"

%}


%include "CS499/get_time.h"
GR_SWIG_BLOCK_MAGIC2(CS499, get_time);

