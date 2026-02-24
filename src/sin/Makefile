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

all: sin.eps sin.pdf sin.png

sin.eps: sin.gle
	gle -device EPS -cairo sin.gle

sin.pdf: sin.gle
	gle -device PDF -cairo sin.gle

sin.png: sin.gle
	gle -device PNG -cairo -DPI 150 sin.gle

clean:
	-$(RM) sin.eps sin.pdf sin.png
	-$(RMDIR) .gle