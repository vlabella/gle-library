#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# -- automatically generated - do not modify all changes maybe lost
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

all: M4_Re_Im.eps M4_Re_Im.pdf M4_Re_Im.png

M4_Re_Im.eps: M4_Re_Im.gle
	gle -device EPS -cairo M4_Re_Im.gle

M4_Re_Im.pdf: M4_Re_Im.gle
	gle -device PDF -cairo M4_Re_Im.gle

M4_Re_Im.png: M4_Re_Im.gle
	gle -device PNG -cairo -DPI 150 M4_Re_Im.gle

clean:
	-$(RM) M4_Re_Im.eps M4_Re_Im.pdf M4_Re_Im.png
	-$(RMDIR) .gle