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

all: barcode_example.eps barcode_example.pdf barcode_example.png

barcode_example.eps: barcode_example.gle
	gle -device EPS -cairo barcode_example.gle

barcode_example.pdf: barcode_example.gle
	gle -device PDF -cairo barcode_example.gle

barcode_example.png: barcode_example.gle
	gle -device PNG -cairo -DPI 150 barcode_example.gle

clean:
	-$(RM) barcode_example.eps barcode_example.pdf barcode_example.png
	-$(RMDIR) .gle