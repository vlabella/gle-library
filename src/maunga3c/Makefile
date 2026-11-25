#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# -- automatically generated - do not modify all changes maybe lost
#
# NMAKE code here \
!ifndef 0 # \
MV=move # \
RM=del /Q # \
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

all: maunga3c.eps maunga3c.pdf maunga3c.png

maunga3c.eps: maunga3c.gle
	gle -device EPS  maunga3c.gle

eps: maunga3c.eps

maunga3c.pdf: maunga3c.gle
	gle -device PDF  maunga3c.gle

pdf: maunga3c.pdf

maunga3c.png: maunga3c.gle
	gle -device PNG -DPI 150 maunga3c.gle

png: maunga3c.png

clean:
	-$(RM) maunga3c.eps maunga3c.pdf maunga3c.png
	-$(RMDIR) .gle