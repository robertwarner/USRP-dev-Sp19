INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MYBLOCK myBlock)

FIND_PATH(
    MYBLOCK_INCLUDE_DIRS
    NAMES myBlock/api.h
    HINTS $ENV{MYBLOCK_DIR}/include
        ${PC_MYBLOCK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MYBLOCK_LIBRARIES
    NAMES gnuradio-myBlock
    HINTS $ENV{MYBLOCK_DIR}/lib
        ${PC_MYBLOCK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MYBLOCK DEFAULT_MSG MYBLOCK_LIBRARIES MYBLOCK_INCLUDE_DIRS)
MARK_AS_ADVANCED(MYBLOCK_LIBRARIES MYBLOCK_INCLUDE_DIRS)

