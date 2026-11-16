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

all: brewersample.eps brewersample.pdf brewersample.png

brewersample.eps: brewersample.gle
	gle -device EPS  brewersample.gle

eps: brewersample.eps

brewersample.pdf: brewersample.gle
	gle -device PDF  brewersample.gle

pdf: brewersample.pdf

brewersample.png: brewersample.gle
	gle -device PNG -DPI 150 brewersample.gle

png: brewersample.png

clean:
	-$(RM) brewersample.eps brewersample.pdf brewersample.png
	-$(RMDIR) .gle