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

all: saddlecol.eps saddlecol.pdf saddlecol.png

saddlecol.eps: saddlecol.gle
	gle -device EPS  saddlecol.gle

eps: saddlecol.eps

saddlecol.pdf: saddlecol.gle
	gle -device PDF  saddlecol.gle

pdf: saddlecol.pdf

saddlecol.png: saddlecol.gle
	gle -device PNG -DPI 150 saddlecol.gle

png: saddlecol.png

clean:
	-$(RM) saddlecol.eps saddlecol.pdf saddlecol.png
	-$(RMDIR) .gle