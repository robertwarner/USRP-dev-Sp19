INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_CS499 CS499)

FIND_PATH(
    CS499_INCLUDE_DIRS
    NAMES CS499/api.h
    HINTS $ENV{CS499_DIR}/include
        ${PC_CS499_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    CS499_LIBRARIES
    NAMES gnuradio-CS499
    HINTS $ENV{CS499_DIR}/lib
        ${PC_CS499_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(CS499 DEFAULT_MSG CS499_LIBRARIES CS499_INCLUDE_DIRS)
MARK_AS_ADVANCED(CS499_LIBRARIES CS499_INCLUDE_DIRS)

