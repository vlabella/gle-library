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

all: markers.eps markers.pdf markers.png

markers.eps: markers.gle
	gle -device EPS  markers.gle

eps: markers.eps

markers.pdf: markers.gle
	gle -device PDF  markers.gle

pdf: markers.pdf

markers.png: markers.gle
	gle -device PNG -DPI 150 markers.gle

png: markers.png

clean:
	-$(RM) markers.eps markers.pdf markers.png
	-$(RMDIR) .gle