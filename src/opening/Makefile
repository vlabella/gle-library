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

all: opening.eps opening.pdf opening.png

opening.eps: opening.gle
	gle -device EPS -cairo opening.gle

opening.pdf: opening.gle
	gle -device PDF -cairo opening.gle

opening.png: opening.gle
	gle -device PNG -cairo -DPI 150 opening.gle

clean:
	-$(RM) opening.eps opening.pdf opening.png
	-$(RMDIR) .gle