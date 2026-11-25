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

all: data.eps data.pdf data.png

data.eps: data.gle
	gle -device EPS -cairo  data.gle

eps: data.eps

data.pdf: data.gle
	gle -device PDF -cairo  data.gle

pdf: data.pdf

data.png: data.gle
	gle -device PNG -cairo -DPI 150 data.gle

png: data.png

clean:
	-$(RM) data.eps data.pdf data.png
	-$(RMDIR) .gle