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

all: bar_chart.eps bar_chart.pdf bar_chart.png

bar_chart.eps: bar_chart.gle
	gle -device EPS -cairo bar_chart.gle

bar_chart.pdf: bar_chart.gle
	gle -device PDF -cairo bar_chart.gle

bar_chart.png: bar_chart.gle
	gle -device PNG -cairo -DPI 150 bar_chart.gle

clean:
	-$(RM) bar_chart.eps bar_chart.pdf bar_chart.png
	-$(RMDIR) .gle