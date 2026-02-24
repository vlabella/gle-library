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

all: color_list_svg.eps color_list_svg.pdf color_list_svg.png

color_list_svg.eps: color_list_svg.gle
	gle -device EPS -cairo color_list_svg.gle

color_list_svg.pdf: color_list_svg.gle
	gle -device PDF -cairo color_list_svg.gle

color_list_svg.png: color_list_svg.gle
	gle -device PNG -cairo -DPI 150 color_list_svg.gle

clean:
	-$(RM) color_list_svg.eps color_list_svg.pdf color_list_svg.png
	-$(RMDIR) .gle