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

all: volcano.eps volcano.pdf volcano.png

volcano.eps: volcano.gle
	gle -device EPS -cairo volcano.gle

volcano.pdf: volcano.gle
	gle -device PDF -cairo volcano.gle

volcano.png: volcano.gle
	gle -device PNG -cairo -DPI 150 volcano.gle

clean:
	-$(RM) volcano.eps volcano.pdf volcano.png
	-$(RMDIR) .gle