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

all: saddle.eps saddle.pdf saddle.png

saddle.eps: saddle.gle
	gle -device EPS -cairo saddle.gle

saddle.pdf: saddle.gle
	gle -device PDF -cairo saddle.gle

saddle.png: saddle.gle
	gle -device PNG -cairo -DPI 150 saddle.gle

clean:
	-$(RM) saddle.eps saddle.pdf saddle.png
	-$(RMDIR) .gle