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

all: super-ellipse.eps super-ellipse.pdf super-ellipse.png

super-ellipse.eps: super-ellipse.gle
	gle -device EPS  super-ellipse.gle

eps: super-ellipse.eps

super-ellipse.pdf: super-ellipse.gle
	gle -device PDF  super-ellipse.gle

pdf: super-ellipse.pdf

super-ellipse.png: super-ellipse.gle
	gle -device PNG -DPI 150 super-ellipse.gle

png: super-ellipse.png

clean:
	-$(RM) super-ellipse.eps super-ellipse.pdf super-ellipse.png
	-$(RMDIR) .gle