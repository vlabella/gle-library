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

all: bitmap.eps bitmap.pdf bitmap.png

bitmap.eps: bitmap.gle
	gle -device EPS -cairo bitmap.gle

bitmap.pdf: bitmap.gle
	gle -device PDF -cairo bitmap.gle

bitmap.png: bitmap.gle
	gle -device PNG -cairo -DPI 150 bitmap.gle

clean:
	-$(RM) bitmap.eps bitmap.pdf bitmap.png
	-$(RMDIR) .gle