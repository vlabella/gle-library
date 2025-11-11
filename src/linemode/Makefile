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

all: linemode.eps linemode.pdf linemode.png

linemode.eps: linemode.gle
	gle -device EPS -cairo linemode.gle

linemode.pdf: linemode.gle
	gle -device PDF -cairo linemode.gle

linemode.png: linemode.gle
	gle -device PNG -cairo -DPI 150 linemode.gle

clean:
	-$(RM) linemode.eps linemode.pdf linemode.png
	-$(RMDIR) .gle