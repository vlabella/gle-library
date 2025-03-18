#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# automatically generated - do not modify all changes maybe lost
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
INSTALL_INCLUDES=copy ..\include\*.gle "C:\Program Files\gle\gleinc" # \
!else
# Make code here
MV=mv -f
RM=rm -f
RMDIR=rm -r
CP=cp -f
MAKE=make
SEP=/
CSEP=;
INSTALL_INCLUDES=sudo cp ../include/*.gle /usr/share/gle/gleinc
# !endif

all: winding.eps winding.pdf winding.png

winding.eps: winding.gle
	gle -device EPS -cairo winding.gle

winding.pdf: winding.gle
	gle -device PDF -cairo winding.gle

winding.png: winding.gle
	gle -device PNG -cairo -DPI 150 winding.gle

clean:
	-$(RM) winding.eps winding.pdf winding.png
	-$(RMDIR) .gle