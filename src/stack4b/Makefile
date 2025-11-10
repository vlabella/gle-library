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

all: stack4b.eps stack4b.pdf stack4b.png

stack4b.eps: stack4b.gle
	gle -device EPS -cairo stack4b.gle

stack4b.pdf: stack4b.gle
	gle -device PDF -cairo stack4b.gle

stack4b.png: stack4b.gle
	gle -device PNG -cairo -DPI 150 stack4b.gle

clean:
	-$(RM) stack4b.eps stack4b.pdf stack4b.png
	-$(RMDIR) .gle