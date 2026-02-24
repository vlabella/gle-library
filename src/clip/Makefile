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

all: clip.eps clip.pdf clip.png

clip.eps: clip.gle
	gle -device EPS -cairo clip.gle

clip.pdf: clip.gle
	gle -device PDF -cairo clip.gle

clip.png: clip.gle
	gle -device PNG -cairo -DPI 150 clip.gle

clean:
	-$(RM) clip.eps clip.pdf clip.png
	-$(RMDIR) .gle