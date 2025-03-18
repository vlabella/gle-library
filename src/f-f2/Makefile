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

all: f-f2.eps f-f2.pdf f-f2.png

f-f2.eps: f-f2.gle
	gle -device EPS -cairo f-f2.gle

f-f2.pdf: f-f2.gle
	gle -device PDF -cairo f-f2.gle

f-f2.png: f-f2.gle
	gle -device PNG -cairo -DPI 150 f-f2.gle

clean:
	-$(RM) f-f2.eps f-f2.pdf f-f2.png
	-$(RMDIR) .gle