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


#ifndef INCLUDED_CS499_GET_TIME_H
#define INCLUDED_CS499_GET_TIME_H

#include <CS499/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace CS499 {

    /*!
     * \brief <+description of block+>
     * \ingroup CS499
     *
     */
    class CS499_API get_time : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<get_time> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of CS499::get_time.
       *
       * To avoid accidental use of raw pointers, CS499::get_time's
       * constructor is in a private implementation
       * class. CS499::get_time::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace CS499
} // namespace gr

#endif /* INCLUDED_CS499_GET_TIME_H */

