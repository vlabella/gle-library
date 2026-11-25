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

all: saddle.eps saddle.pdf saddle.png

saddle.eps: saddle.gle
	gle -device EPS -cairo  saddle.gle

eps: saddle.eps

saddle.pdf: saddle.gle
	gle -device PDF -cairo  saddle.gle

pdf: saddle.pdf

saddle.png: saddle.gle
	gle -device PNG -cairo -DPI 150 saddle.gle

png: saddle.png

clean:
	-$(RM) saddle.eps saddle.pdf saddle.png
	-$(RMDIR) .gle