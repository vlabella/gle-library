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

all: volcano3d.eps volcano3d.pdf volcano3d.png

volcano3d.eps: volcano3d.gle
	gle -device EPS -cairo volcano3d.gle

volcano3d.pdf: volcano3d.gle
	gle -device PDF -cairo volcano3d.gle

volcano3d.png: volcano3d.gle
	gle -device PNG -cairo -DPI 150 volcano3d.gle

clean:
	-$(RM) volcano3d.eps volcano3d.pdf volcano3d.png
	-$(RMDIR) .gle