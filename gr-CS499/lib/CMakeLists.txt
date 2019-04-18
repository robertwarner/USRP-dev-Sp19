# Copyright 2011,2012,2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND CS499_sources
    get_time_impl.cc
)

set(CS499_sources "${CS499_sources}" PARENT_SCOPE)
if(NOT CS499_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT CS499_sources)

add_library(gnuradio-CS499 SHARED ${CS499_sources})
target_link_libraries(gnuradio-CS499 ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-CS499 PROPERTIES DEFINE_SYMBOL "gnuradio_CS499_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-CS499 PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-CS499 RUNTIME_COMPONENT "CS499_runtime" DEVEL_COMPONENT "CS499_devel")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_CS499_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_CS499.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_CS499.cc
)

add_executable(test-CS499 ${test_CS499_sources})

target_link_libraries(
  test-CS499
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-CS499
)

GR_ADD_TEST(test_CS499 test-CS499)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

