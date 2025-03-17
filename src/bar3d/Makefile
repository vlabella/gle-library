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

all: bar3d.eps bar3d.pdf bar3d.png

bar3d.eps: bar3d.gle
	gle -device EPS -cairo bar3d.gle

bar3d.pdf: bar3d.gle
	gle -device PDF -cairo bar3d.gle

bar3d.png: bar3d.gle
	gle -device PNG -cairo -DPI 150 bar3d.gle

clean:
	-$(RM) bar3d.eps bar3d.pdf bar3d.png
	-$(RMDIR) .gle