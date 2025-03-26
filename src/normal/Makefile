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

all: normal.eps normal.pdf normal.png

normal.eps: normal.gle
	gle -device EPS -cairo normal.gle

normal.pdf: normal.gle
	gle -device PDF -cairo normal.gle

normal.png: normal.gle
	gle -device PNG -cairo -DPI 150 normal.gle

clean:
	-$(RM) normal.eps normal.pdf normal.png
	-$(RMDIR) .gle