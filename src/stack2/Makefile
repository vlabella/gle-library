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

all: stack2.eps stack2.pdf stack2.png

stack2.eps: stack2.gle
	gle -device EPS -cairo stack2.gle

stack2.pdf: stack2.gle
	gle -device PDF -cairo stack2.gle

stack2.png: stack2.gle
	gle -device PNG -cairo -DPI 150 stack2.gle

clean:
	-$(RM) stack2.eps stack2.pdf stack2.png
	-$(RMDIR) .gle