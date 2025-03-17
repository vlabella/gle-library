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

all: loop.eps loop.pdf loop.png

loop.eps: loop.gle
	gle -device EPS -cairo loop.gle

loop.pdf: loop.gle
	gle -device PDF -cairo loop.gle

loop.png: loop.gle
	gle -device PNG -cairo -DPI 150 loop.gle

clean:
	-$(RM) loop.eps loop.pdf loop.png
	-$(RMDIR) .gle