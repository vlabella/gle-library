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

all: wall.eps wall.pdf wall.png

wall.eps: wall.gle
	gle -device EPS -cairo wall.gle

wall.pdf: wall.gle
	gle -device PDF -cairo wall.gle

wall.png: wall.gle
	gle -device PNG -cairo -DPI 150 wall.gle

clean:
	-$(RM) wall.eps wall.pdf wall.png
	-$(RMDIR) .gle