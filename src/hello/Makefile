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
!endif

install-includes:
	$(INSTALL_INCLUDES)

all: hello.eps hello.pdf hello.png

hello.eps: hello.gle
	gle -device EPS -cairo hello.gle

hello.pdf: hello.gle
	gle -device PDF -cairo hello.gle

hello.png: hello.gle
	gle -device PNG -cairo -DPI 150 hello.gle

clean:
	-$(RM) hello.eps hello.pdf hello.png
	-$(RMDIR) .gle