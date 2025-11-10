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

all: filters81.eps filters81.pdf filters81.png

filters81.eps: filters81.gle
	gle -device EPS -cairo filters81.gle

filters81.pdf: filters81.gle
	gle -device PDF -cairo filters81.gle

filters81.png: filters81.gle
	gle -device PNG -cairo -DPI 150 filters81.gle

clean:
	-$(RM) filters81.eps filters81.pdf filters81.png
	-$(RMDIR) .gle