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

all: lnx.eps lnx.pdf lnx.png

lnx.eps: lnx.gle
	gle -device EPS -cairo  lnx.gle

eps: lnx.eps

lnx.pdf: lnx.gle
	gle -device PDF -cairo  lnx.gle

pdf: lnx.pdf

lnx.png: lnx.gle
	gle -device PNG -cairo -DPI 150 lnx.gle

png: lnx.png

clean:
	-$(RM) lnx.eps lnx.pdf lnx.png
	-$(RMDIR) .gle