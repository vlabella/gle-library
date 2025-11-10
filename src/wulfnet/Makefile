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

all: wulfnet.eps wulfnet.pdf wulfnet.png

wulfnet.eps: wulfnet.gle
	gle -device EPS -cairo wulfnet.gle

wulfnet.pdf: wulfnet.gle
	gle -device PDF -cairo wulfnet.gle

wulfnet.png: wulfnet.gle
	gle -device PNG -cairo -DPI 150 wulfnet.gle

clean:
	-$(RM) wulfnet.eps wulfnet.pdf wulfnet.png
	-$(RMDIR) .gle