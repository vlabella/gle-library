#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# -- automatically generated - do not modify all changes maybe lost
#
# NMAKE code here \
!ifndef 0 # \
MV=move # \
RM=del /Q # \
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
	gle -device EPS  spectrum.gle

eps: spectrum.eps

spectrum.pdf: spectrum.gle
	gle -device PDF  spectrum.gle

pdf: spectrum.pdf

spectrum.png: spectrum.gle
	gle -device PNG -DPI 150 spectrum.gle

png: spectrum.png

clean:
	-$(RM) spectrum.eps spectrum.pdf spectrum.png
	-$(RMDIR) .gle