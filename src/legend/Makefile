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

all: legend.eps legend.pdf legend.png

legend.eps: legend.gle
	gle -device EPS -cairo  legend.gle

eps: legend.eps

legend.pdf: legend.gle
	gle -device PDF -cairo  legend.gle

pdf: legend.pdf

legend.png: legend.gle
	gle -device PNG -cairo -DPI 150 legend.gle

png: legend.png

clean:
	-$(RM) legend.eps legend.pdf legend.png
	-$(RMDIR) .gle