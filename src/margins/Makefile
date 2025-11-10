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

all: margins.eps margins.pdf margins.png

margins.eps: margins.gle
	gle -device EPS -cairo margins.gle

margins.pdf: margins.gle
	gle -device PDF -cairo margins.gle

margins.png: margins.gle
	gle -device PNG -cairo -DPI 150 margins.gle

clean:
	-$(RM) margins.eps margins.pdf margins.png
	-$(RMDIR) .gle