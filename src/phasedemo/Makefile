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

all: phasedemo.eps phasedemo.pdf phasedemo.png

phasedemo.eps: phasedemo.gle
	gle -device EPS -cairo phasedemo.gle

phasedemo.pdf: phasedemo.gle
	gle -device PDF -cairo phasedemo.gle

phasedemo.png: phasedemo.gle
	gle -device PNG -cairo -DPI 150 phasedemo.gle

clean:
	-$(RM) phasedemo.eps phasedemo.pdf phasedemo.png
	-$(RMDIR) .gle