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

all: lines.eps lines.pdf lines.png

lines.eps: lines.gle
	gle -device EPS -cairo lines.gle

lines.pdf: lines.gle
	gle -device PDF -cairo lines.gle

lines.png: lines.gle
	gle -device PNG -cairo -DPI 150 lines.gle

clean:
	-$(RM) lines.eps lines.pdf lines.png
	-$(RMDIR) .gle