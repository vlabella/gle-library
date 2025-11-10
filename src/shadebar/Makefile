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

all: shadebar.eps shadebar.pdf shadebar.png

shadebar.eps: shadebar.gle
	gle -device EPS -cairo shadebar.gle

shadebar.pdf: shadebar.gle
	gle -device PDF -cairo shadebar.gle

shadebar.png: shadebar.gle
	gle -device PNG -cairo -DPI 150 shadebar.gle

clean:
	-$(RM) shadebar.eps shadebar.pdf shadebar.png
	-$(RMDIR) .gle