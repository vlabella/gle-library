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

all: equation.eps equation.pdf equation.png

equation.eps: equation.gle
	gle -device EPS -cairo equation.gle

equation.pdf: equation.gle
	gle -device PDF -cairo equation.gle

equation.png: equation.gle
	gle -device PNG -cairo -DPI 150 equation.gle

clean:
	-$(RM) equation.eps equation.pdf equation.png
	-$(RMDIR) .gle