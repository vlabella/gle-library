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

all: recursiontree.eps recursiontree.pdf recursiontree.png

recursiontree.eps: recursiontree.gle
	gle -device EPS -cairo recursiontree.gle

recursiontree.pdf: recursiontree.gle
	gle -device PDF -cairo recursiontree.gle

recursiontree.png: recursiontree.gle
	gle -device PNG -cairo -DPI 150 recursiontree.gle

clean:
	-$(RM) recursiontree.eps recursiontree.pdf recursiontree.png
	-$(RMDIR) .gle