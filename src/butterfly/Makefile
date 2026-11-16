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

all: butterfly.eps butterfly.pdf butterfly.png

butterfly.eps: butterfly.gle
	gle -device EPS -cairo  butterfly.gle

eps: butterfly.eps

butterfly.pdf: butterfly.gle
	gle -device PDF -cairo  butterfly.gle

pdf: butterfly.pdf

butterfly.png: butterfly.gle
	gle -device PNG -cairo -DPI 150 butterfly.gle

png: butterfly.png

clean:
	-$(RM) butterfly.eps butterfly.pdf butterfly.png
	-$(RMDIR) .gle