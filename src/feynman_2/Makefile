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

all: feynman_2.eps feynman_2.pdf feynman_2.png

feynman_2.eps: feynman_2.gle
	gle -device EPS -cairo feynman_2.gle

feynman_2.pdf: feynman_2.gle
	gle -device PDF -cairo feynman_2.gle

feynman_2.png: feynman_2.gle
	gle -device PNG -cairo -DPI 150 feynman_2.gle

clean:
	-$(RM) feynman_2.eps feynman_2.pdf feynman_2.png
	-$(RMDIR) .gle