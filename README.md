# gle-library

GLE Library - Library of figures and include files for [GLE](http://glx.sourceforge.io).  The include files come bundled with the GLE distribution.  However, they may get updated prior to the next release.  This repo makes them available separately for users to modify and/or update outside of the GLE release schedule.  In addition it enealbes users to contribute thier own routines and sample figures.  See instructions below.

## Installation Instructions

Installation of include files is only needed if they get updted prior to the next release of GLE. The installation command below copies all the .gle files from /include to the /gleinc folder at the root of your GLE installation:

* windows: `C:\Program Files\GLE\gleinc`.
* Linux: `/usr/share/gle/gleinc`.

To install the new include files

 `cd src` & `make install-includes` or `nmake install-includes`

## Building all figures

To build all the figures

  `cd src` & `make` or `nmake`

To clean the build

  `cd src` & `make clean` or `nmake clean`

## Contributing Figures


## Contributing Include Files


## Regenerating the Makefile
