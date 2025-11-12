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

all: brilzone.eps brilzone.pdf brilzone.png

brilzone.eps: brilzone.gle
	gle -device EPS -cairo brilzone.gle

brilzone.pdf: brilzone.gle
	gle -device PDF -cairo brilzone.gle

brilzone.png: brilzone.gle
	gle -device PNG -cairo -DPI 150 brilzone.gle

clean:
	-$(RM) brilzone.eps brilzone.pdf brilzone.png
	-$(RMDIR) .gle