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

all: parallel.eps parallel.pdf parallel.png

parallel.eps: parallel.gle
	gle -device EPS -cairo parallel.gle

parallel.pdf: parallel.gle
	gle -device PDF -cairo parallel.gle

parallel.png: parallel.gle
	gle -device PNG -cairo -DPI 150 parallel.gle

clean:
	-$(RM) parallel.eps parallel.pdf parallel.png
	-$(RMDIR) .gle