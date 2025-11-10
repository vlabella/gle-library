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

all: rt-y-is-x.eps rt-y-is-x.pdf rt-y-is-x.png

rt-y-is-x.eps: rt-y-is-x.gle
	gle -device EPS -cairo rt-y-is-x.gle

rt-y-is-x.pdf: rt-y-is-x.gle
	gle -device PDF -cairo rt-y-is-x.gle

rt-y-is-x.png: rt-y-is-x.gle
	gle -device PNG -cairo -DPI 150 rt-y-is-x.gle

clean:
	-$(RM) rt-y-is-x.eps rt-y-is-x.pdf rt-y-is-x.png
	-$(RMDIR) .gle