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

all: let-multi-dim.eps let-multi-dim.pdf let-multi-dim.png

let-multi-dim.eps: let-multi-dim.gle
	gle -device EPS -cairo let-multi-dim.gle

let-multi-dim.pdf: let-multi-dim.gle
	gle -device PDF -cairo let-multi-dim.gle

let-multi-dim.png: let-multi-dim.gle
	gle -device PNG -cairo -DPI 150 let-multi-dim.gle

clean:
	-$(RM) let-multi-dim.eps let-multi-dim.pdf let-multi-dim.png
	-$(RMDIR) .gle