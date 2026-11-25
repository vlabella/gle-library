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

all: dragon.eps dragon.pdf dragon.png

dragon.eps: dragon.gle
	gle -device EPS -cairo  dragon.gle

eps: dragon.eps

dragon.pdf: dragon.gle
	gle -device PDF -cairo  dragon.gle

pdf: dragon.pdf

dragon.png: dragon.gle
	gle -device PNG -cairo -DPI 150 dragon.gle

png: dragon.png

clean:
	-$(RM) dragon.eps dragon.pdf dragon.png
	-$(RMDIR) .gle