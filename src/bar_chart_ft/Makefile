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

all: bar_chart_ft.eps bar_chart_ft.pdf bar_chart_ft.png

bar_chart_ft.eps: bar_chart_ft.gle
	gle -device EPS -cairo bar_chart_ft.gle

bar_chart_ft.pdf: bar_chart_ft.gle
	gle -device PDF -cairo bar_chart_ft.gle

bar_chart_ft.png: bar_chart_ft.gle
	gle -device PNG -cairo -DPI 150 bar_chart_ft.gle

clean:
	-$(RM) bar_chart_ft.eps bar_chart_ft.pdf bar_chart_ft.png
	-$(RMDIR) .gle