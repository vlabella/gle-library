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

all: horizon.eps horizon.pdf horizon.png

horizon.eps: horizon.gle
	gle -device EPS -cairo  horizon.gle

eps: horizon.eps

horizon.pdf: horizon.gle
	gle -device PDF -cairo  horizon.gle

pdf: horizon.pdf

horizon.png: horizon.gle
	gle -device PNG -cairo -DPI 150 horizon.gle

png: horizon.png

clean:
	-$(RM) horizon.eps horizon.pdf horizon.png
	-$(RMDIR) .gle