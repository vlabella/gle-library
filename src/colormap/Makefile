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
!endif

install-includes:
	$(INSTALL_INCLUDES)

all: colormap.eps colormap.pdf colormap.png

colormap.eps: colormap.gle
	gle -device EPS -cairo colormap.gle

colormap.pdf: colormap.gle
	gle -device PDF -cairo colormap.gle

colormap.png: colormap.gle
	gle -device PNG -cairo -DPI 150 colormap.gle

clean:
	-$(RM) colormap.eps colormap.pdf colormap.png
	-$(RMDIR) .gle