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

all: horizon.eps horizon.pdf horizon.png

horizon.eps: horizon.gle
	gle -device EPS -cairo horizon.gle

horizon.pdf: horizon.gle
	gle -device PDF -cairo horizon.gle

horizon.png: horizon.gle
	gle -device PNG -cairo -DPI 150 horizon.gle

clean:
	-$(RM) horizon.eps horizon.pdf horizon.png
	-$(RMDIR) .gle