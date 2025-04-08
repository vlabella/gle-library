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

all: nottingham.eps nottingham.pdf nottingham.png

nottingham.eps: nottingham.gle
	gle -device EPS -cairo nottingham.gle

nottingham.pdf: nottingham.gle
	gle -device PDF -cairo nottingham.gle

nottingham.png: nottingham.gle
	gle -device PNG -cairo -DPI 150 nottingham.gle

clean:
	-$(RM) nottingham.eps nottingham.pdf nottingham.png
	-$(RMDIR) .gle