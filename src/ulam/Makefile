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

all: ulam.eps ulam.pdf ulam.png

ulam.eps: ulam.gle
	gle -device EPS  ulam.gle

eps: ulam.eps

ulam.pdf: ulam.gle
	gle -device PDF  ulam.gle

pdf: ulam.pdf

ulam.png: ulam.gle
	gle -device PNG -DPI 150 ulam.gle

png: ulam.png

clean:
	-$(RM) ulam.eps ulam.pdf ulam.png
	-$(RMDIR) .gle