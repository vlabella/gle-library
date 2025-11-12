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

all: adjust.eps adjust.pdf adjust.png

adjust.eps: adjust.gle
	gle -device EPS -cairo adjust.gle

adjust.pdf: adjust.gle
	gle -device PDF -cairo adjust.gle

adjust.png: adjust.gle
	gle -device PNG -cairo -DPI 150 adjust.gle

clean:
	-$(RM) adjust.eps adjust.pdf adjust.png
	-$(RMDIR) .gle