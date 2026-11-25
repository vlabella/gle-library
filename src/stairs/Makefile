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

all: stairs.eps stairs.pdf stairs.png

stairs.eps: stairs.gle
	gle -device EPS  stairs.gle

eps: stairs.eps

stairs.pdf: stairs.gle
	gle -device PDF  stairs.gle

pdf: stairs.pdf

stairs.png: stairs.gle
	gle -device PNG -DPI 150 stairs.gle

png: stairs.png

clean:
	-$(RM) stairs.eps stairs.pdf stairs.png
	-$(RMDIR) .gle