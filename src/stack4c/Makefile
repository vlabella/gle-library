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

all: stack4c.eps stack4c.pdf stack4c.png

stack4c.eps: stack4c.gle
	gle -device EPS -cairo stack4c.gle

stack4c.pdf: stack4c.gle
	gle -device PDF -cairo stack4c.gle

stack4c.png: stack4c.gle
	gle -device PNG -cairo -DPI 150 stack4c.gle

clean:
	-$(RM) stack4c.eps stack4c.pdf stack4c.png
	-$(RMDIR) .gle