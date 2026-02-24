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

all: quantilescale.eps quantilescale.pdf quantilescale.png

quantilescale.eps: quantilescale.gle
	gle -device EPS -cairo quantilescale.gle

quantilescale.pdf: quantilescale.gle
	gle -device PDF -cairo quantilescale.gle

quantilescale.png: quantilescale.gle
	gle -device PNG -cairo -DPI 150 quantilescale.gle

clean:
	-$(RM) quantilescale.eps quantilescale.pdf quantilescale.png
	-$(RMDIR) .gle