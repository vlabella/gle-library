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

all: clip-ft.eps clip-ft.pdf clip-ft.png

clip-ft.eps: clip-ft.gle
	gle -device EPS -cairo clip-ft.gle

clip-ft.pdf: clip-ft.gle
	gle -device PDF -cairo clip-ft.gle

clip-ft.png: clip-ft.gle
	gle -device PNG -cairo -DPI 150 clip-ft.gle

clean:
	-$(RM) clip-ft.eps clip-ft.pdf clip-ft.png
	-$(RMDIR) .gle