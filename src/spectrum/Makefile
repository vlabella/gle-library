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

all: spectrum.eps spectrum.pdf spectrum.png

spectrum.eps: spectrum.gle
	gle -device EPS -cairo spectrum.gle

spectrum.pdf: spectrum.gle
	gle -device PDF -cairo spectrum.gle

spectrum.png: spectrum.gle
	gle -device PNG -cairo -DPI 150 spectrum.gle

clean:
	-$(RM) spectrum.eps spectrum.pdf spectrum.png
	-$(RMDIR) .gle