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

all: ramps.eps ramps.pdf ramps.png

ramps.eps: ramps.gle
	gle -device EPS -cairo ramps.gle

ramps.pdf: ramps.gle
	gle -device PDF -cairo ramps.gle

ramps.png: ramps.gle
	gle -device PNG -cairo -DPI 150 ramps.gle

clean:
	-$(RM) ramps.eps ramps.pdf ramps.png
	-$(RMDIR) .gle