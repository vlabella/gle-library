#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# -- automatically generated - do not modify all changes maybe lost
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
INSTALL_INCLUDES=copy ..\include\*.gle "C:\Program Files\gle-graphics\gleinc" # \
!else
# Make code here
MV=mv -f
RM=rm -f
RMDIR=rm -r
CP=cp -f
MAKE=make
SEP=/
CSEP=;
INSTALL_INCLUDES=sudo cp ../include/*.gle /usr/share/gle-graphics/gleinc
# \
!endif

all: RGB_gaph.eps RGB_gaph.pdf RGB_gaph.png

RGB_gaph.eps: RGB_gaph.gle
	gle -device EPS -cairo RGB_gaph.gle

RGB_gaph.pdf: RGB_gaph.gle
	gle -device PDF -cairo RGB_gaph.gle

RGB_gaph.png: RGB_gaph.gle
	gle -device PNG -cairo -DPI 150 RGB_gaph.gle

clean:
	-$(RM) RGB_gaph.eps RGB_gaph.pdf RGB_gaph.png
	-$(RMDIR) .gle