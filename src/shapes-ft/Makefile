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

all: shapes-ft.eps shapes-ft.pdf shapes-ft.png

shapes-ft.eps: shapes-ft.gle
	gle -device EPS -cairo shapes-ft.gle

shapes-ft.pdf: shapes-ft.gle
	gle -device PDF -cairo shapes-ft.gle

shapes-ft.png: shapes-ft.gle
	gle -device PNG -cairo -DPI 150 shapes-ft.gle

clean:
	-$(RM) shapes-ft.eps shapes-ft.pdf shapes-ft.png
	-$(RMDIR) .gle