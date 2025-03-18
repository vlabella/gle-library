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

all: colorspaces.eps colorspaces.pdf colorspaces.png

colorspaces.eps: colorspaces.gle
	gle -device EPS -cairo colorspaces.gle

colorspaces.pdf: colorspaces.gle
	gle -device PDF -cairo colorspaces.gle

colorspaces.png: colorspaces.gle
	gle -device PNG -cairo -DPI 150 colorspaces.gle

clean:
	-$(RM) colorspaces.eps colorspaces.pdf colorspaces.png
	-$(RMDIR) .gle