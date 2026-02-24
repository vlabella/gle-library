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

all: decay.eps decay.pdf decay.png

decay.eps: decay.gle
	gle -device EPS -cairo decay.gle

decay.pdf: decay.gle
	gle -device PDF -cairo decay.gle

decay.png: decay.gle
	gle -device PNG -cairo -DPI 150 decay.gle

clean:
	-$(RM) decay.eps decay.pdf decay.png
	-$(RMDIR) .gle