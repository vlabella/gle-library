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

all: brics.eps brics.pdf brics.png

brics.eps: brics.gle
	gle -device EPS  brics.gle

eps: brics.eps

brics.pdf: brics.gle
	gle -device PDF  brics.gle

pdf: brics.pdf

brics.png: brics.gle
	gle -device PNG -DPI 150 brics.gle

png: brics.png

clean:
	-$(RM) brics.eps brics.pdf brics.png
	-$(RMDIR) .gle