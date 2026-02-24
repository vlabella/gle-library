#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# automatically generated - do not modify all changes maybe lost
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
INSTALL_INCLUDES=copy ..\include\*.gle "C:\Program Files\gle\gleinc" # \
!else
# Make code here
MV=mv -f
RM=rm -f
RMDIR=rm -r
CP=cp -f
MAKE=make
SEP=/
CSEP=;
INSTALL_INCLUDES=sudo cp ../include/*.gle /usr/share/gle/gleinc
# \
!endif

all: pythagoras.eps pythagoras.pdf pythagoras.png

pythagoras.eps: pythagoras.gle
	gle -device EPS -cairo pythagoras.gle

pythagoras.pdf: pythagoras.gle
	gle -device PDF -cairo pythagoras.gle

pythagoras.png: pythagoras.gle
	gle -device PNG -cairo -DPI 150 pythagoras.gle

clean:
	-$(RM) pythagoras.eps pythagoras.pdf pythagoras.png
	-$(RMDIR) .gle