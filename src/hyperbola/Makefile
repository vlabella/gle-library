#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# automatically generated - do not modify all changes maybe lost
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
INSTALL_INCLUDES=copy ..\include\*.gle "C:\Program Files\gle\gleinc" # \
!else
# Make code here
MV=mv -f
RM=rm -f
RMDIR=rm -r
CP=cp -f
MAKE=make
SEP=/
CSEP=;
INSTALL_INCLUDES=sudo cp ../include/*.gle /usr/share/gle/gleinc
# !endif

all: hyperbola.eps hyperbola.pdf hyperbola.png

hyperbola.eps: hyperbola.gle
	gle -device EPS -cairo hyperbola.gle

hyperbola.pdf: hyperbola.gle
	gle -device PDF -cairo hyperbola.gle

hyperbola.png: hyperbola.gle
	gle -device PNG -cairo -DPI 150 hyperbola.gle

clean:
	-$(RM) hyperbola.eps hyperbola.pdf hyperbola.png
	-$(RMDIR) .gle