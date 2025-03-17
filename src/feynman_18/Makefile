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

all: feynman_18.eps feynman_18.pdf feynman_18.png

feynman_18.eps: feynman_18.gle
	gle -device EPS -cairo feynman_18.gle

feynman_18.pdf: feynman_18.gle
	gle -device PDF -cairo feynman_18.gle

feynman_18.png: feynman_18.gle
	gle -device PNG -cairo -DPI 150 feynman_18.gle

clean:
	-$(RM) feynman_18.eps feynman_18.pdf feynman_18.png
	-$(RMDIR) .gle