/* -*- c++ -*- */
/* 
 * Copyright 2019 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "get_time_impl.h"
#include <gnuradio/io_signature.h>
#include <cstdio>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdexcept>
#include <stdio.h>



namespace gr {
  namespace CS499 {

    get_time::sptr
    get_time::make()
    {
      return gnuradio::get_initial_sptr
        (new get_time_impl());
    }

    /*
     * The private constructor
     */
    get_time_impl::get_time_impl()
          : gr::block("get_time",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(1, 1, sizeof(long long)))
    {}

    /*
     * Our virtual destructor.
     */
    get_time_impl::~get_time_impl()
    {
    }


    long long
    get_time_impl::work (int noutput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      std::chrono::high_resolution_clock::time_point finish = std::chrono::high_resolution_clock::now();
      long long elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(finish - start).count();
      return elapsed;
    }

  } /* namespace CS499 */
} /* namespace gr */

