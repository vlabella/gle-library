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

all: polar_plot.eps polar_plot.pdf polar_plot.png

polar_plot.eps: polar_plot.gle
	gle -device EPS -cairo polar_plot.gle

polar_plot.pdf: polar_plot.gle
	gle -device PDF -cairo polar_plot.gle

polar_plot.png: polar_plot.gle
	gle -device PNG -cairo -DPI 150 polar_plot.gle

clean:
	-$(RM) polar_plot.eps polar_plot.pdf polar_plot.png
	-$(RMDIR) .gle