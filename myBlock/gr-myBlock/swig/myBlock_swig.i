/* -*- c++ -*- */

#define MYBLOCK_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "myBlock_swig_doc.i"

%{
#include "myBlock/test.h"
#include "myBlock/my_qpsk_demod_cb.h"
%}


%include "myBlock/test.h"
GR_SWIG_BLOCK_MAGIC2(myBlock, test);
%include "myBlock/my_qpsk_demod_cb.h"
GR_SWIG_BLOCK_MAGIC2(myBlock, my_qpsk_demod_cb);
