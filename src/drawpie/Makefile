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

all: drawpie.eps drawpie.pdf drawpie.png

drawpie.eps: drawpie.gle
	gle -device EPS -cairo drawpie.gle

drawpie.pdf: drawpie.gle
	gle -device PDF -cairo drawpie.gle

drawpie.png: drawpie.gle
	gle -device PNG -cairo -DPI 150 drawpie.gle

clean:
	-$(RM) drawpie.eps drawpie.pdf drawpie.png
	-$(RMDIR) .gle