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

all: color-markers-3d.eps color-markers-3d.pdf color-markers-3d.png

color-markers-3d.eps: color-markers-3d.gle
	gle -device EPS -cairo color-markers-3d.gle

color-markers-3d.pdf: color-markers-3d.gle
	gle -device PDF -cairo color-markers-3d.gle

color-markers-3d.png: color-markers-3d.gle
	gle -device PNG -cairo -DPI 150 color-markers-3d.gle

clean:
	-$(RM) color-markers-3d.eps color-markers-3d.pdf color-markers-3d.png
	-$(RMDIR) .gle