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
# \
!endif

all: math_mode_plot.eps math_mode_plot.pdf math_mode_plot.png

math_mode_plot.eps: math_mode_plot.gle
	gle -device EPS -cairo math_mode_plot.gle

math_mode_plot.pdf: math_mode_plot.gle
	gle -device PDF -cairo math_mode_plot.gle

math_mode_plot.png: math_mode_plot.gle
	gle -device PNG -cairo -DPI 150 math_mode_plot.gle

clean:
	-$(RM) math_mode_plot.eps math_mode_plot.pdf math_mode_plot.png
	-$(RMDIR) .gle