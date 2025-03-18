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

all: fill-ft.eps fill-ft.pdf fill-ft.png

fill-ft.eps: fill-ft.gle
	gle -device EPS -cairo fill-ft.gle

fill-ft.pdf: fill-ft.gle
	gle -device PDF -cairo fill-ft.gle

fill-ft.png: fill-ft.gle
	gle -device PNG -cairo -DPI 150 fill-ft.gle

clean:
	-$(RM) fill-ft.eps fill-ft.pdf fill-ft.png
	-$(RMDIR) .gle