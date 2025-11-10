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
# \
!endif

all: zoom-in.eps zoom-in.pdf zoom-in.png

zoom-in.eps: zoom-in.gle
	gle -device EPS -cairo zoom-in.gle

zoom-in.pdf: zoom-in.gle
	gle -device PDF -cairo zoom-in.gle

zoom-in.png: zoom-in.gle
	gle -device PNG -cairo -DPI 150 zoom-in.gle

clean:
	-$(RM) zoom-in.eps zoom-in.pdf zoom-in.png
	-$(RMDIR) .gle