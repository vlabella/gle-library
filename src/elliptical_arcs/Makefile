#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# -- automatically generated - do not modify all changes maybe lost
#
# NMAKE code here \
!ifndef 0 # \
MV=move # \
RM=del # \
RMDIR=rmdir /S /Q # \
CP=copy # \
MAKE=nmake /nologo # \
SEP=\ # \
CSEP=& # \
INSTALL_INCLUDES=copy ..\include\*.gle "C:\Program Files\gle-graphics\gleinc" # \
!else
# Make code here
MV=mv -f
RM=rm -f
RMDIR=rm -r
CP=cp -f
MAKE=make
SEP=/
CSEP=;
INSTALL_INCLUDES=sudo cp ../include/*.gle /usr/share/gle-graphics/gleinc
# \
!endif

all: elliptical_arcs.eps elliptical_arcs.pdf elliptical_arcs.png

elliptical_arcs.eps: elliptical_arcs.gle
	gle -device EPS -cairo elliptical_arcs.gle

elliptical_arcs.pdf: elliptical_arcs.gle
	gle -device PDF -cairo elliptical_arcs.gle

elliptical_arcs.png: elliptical_arcs.gle
	gle -device PNG -cairo -DPI 150 elliptical_arcs.gle

clean:
	-$(RM) elliptical_arcs.eps elliptical_arcs.pdf elliptical_arcs.png
	-$(RMDIR) .gle