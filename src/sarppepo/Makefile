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

all: sarppepo.eps sarppepo.pdf sarppepo.png

sarppepo.eps: sarppepo.gle
	gle -device EPS -cairo sarppepo.gle

sarppepo.pdf: sarppepo.gle
	gle -device PDF -cairo sarppepo.gle

sarppepo.png: sarppepo.gle
	gle -device PNG -cairo -DPI 150 sarppepo.gle

clean:
	-$(RM) sarppepo.eps sarppepo.pdf sarppepo.png
	-$(RMDIR) .gle