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

all: mesh.eps mesh.pdf mesh.png

mesh.eps: mesh.gle
	gle -device EPS  mesh.gle

eps: mesh.eps

mesh.pdf: mesh.gle
	gle -device PDF  mesh.gle

pdf: mesh.pdf

mesh.png: mesh.gle
	gle -device PNG -DPI 150 mesh.gle

png: mesh.png

clean:
	-$(RM) mesh.eps mesh.pdf mesh.png
	-$(RMDIR) .gle