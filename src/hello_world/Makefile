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

all: hello_world.eps hello_world.pdf hello_world.png

hello_world.eps: hello_world.gle
	gle -device EPS -cairo hello_world.gle

hello_world.pdf: hello_world.gle
	gle -device PDF -cairo hello_world.gle

hello_world.png: hello_world.gle
	gle -device PNG -cairo -DPI 150 hello_world.gle

clean:
	-$(RM) hello_world.eps hello_world.pdf hello_world.png
	-$(RMDIR) .gle