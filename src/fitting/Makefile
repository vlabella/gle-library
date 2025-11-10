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

all: fitting.eps fitting.pdf fitting.png

fitting.eps: fitting.gle
	gle -device EPS -cairo fitting.gle

fitting.pdf: fitting.gle
	gle -device PDF -cairo fitting.gle

fitting.png: fitting.gle
	gle -device PNG -cairo -DPI 150 fitting.gle

clean:
	-$(RM) fitting.eps fitting.pdf fitting.png
	-$(RMDIR) .gle