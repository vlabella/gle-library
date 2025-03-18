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
# !endif

all: gc_color.eps gc_color.pdf gc_color.png

gc_color.eps: gc_color.gle
	gle -device EPS -cairo gc_color.gle

gc_color.pdf: gc_color.gle
	gle -device PDF -cairo gc_color.gle

gc_color.png: gc_color.gle
	gle -device PNG -cairo -DPI 150 gc_color.gle

clean:
	-$(RM) gc_color.eps gc_color.pdf gc_color.png
	-$(RMDIR) .gle