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

all: ellipses.eps ellipses.pdf ellipses.png

ellipses.eps: ellipses.gle
	gle -device EPS -cairo ellipses.gle

ellipses.pdf: ellipses.gle
	gle -device PDF -cairo ellipses.gle

ellipses.png: ellipses.gle
	gle -device PNG -cairo -DPI 150 ellipses.gle

clean:
	-$(RM) ellipses.eps ellipses.pdf ellipses.png
	-$(RMDIR) .gle