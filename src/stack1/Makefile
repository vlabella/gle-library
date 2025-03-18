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

all: stack1.eps stack1.pdf stack1.png

stack1.eps: stack1.gle
	gle -device EPS -cairo stack1.gle

stack1.pdf: stack1.gle
	gle -device PDF -cairo stack1.gle

stack1.png: stack1.gle
	gle -device PNG -cairo -DPI 150 stack1.gle

clean:
	-$(RM) stack1.eps stack1.pdf stack1.png
	-$(RMDIR) .gle