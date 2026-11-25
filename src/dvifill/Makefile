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

all: dvifill.eps dvifill.pdf dvifill.png

dvifill.eps: dvifill.gle
	gle -device EPS -cairo  dvifill.gle

eps: dvifill.eps

dvifill.pdf: dvifill.gle
	gle -device PDF -cairo  dvifill.gle

pdf: dvifill.pdf

dvifill.png: dvifill.gle
	gle -device PNG -cairo -DPI 150 dvifill.gle

png: dvifill.png

clean:
	-$(RM) dvifill.eps dvifill.pdf dvifill.png
	-$(RMDIR) .gle