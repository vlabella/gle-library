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

all: compactkey.eps compactkey.pdf compactkey.png

compactkey.eps: compactkey.gle
	gle -device EPS -cairo compactkey.gle

compactkey.pdf: compactkey.gle
	gle -device PDF -cairo compactkey.gle

compactkey.png: compactkey.gle
	gle -device PNG -cairo -DPI 150 compactkey.gle

clean:
	-$(RM) compactkey.eps compactkey.pdf compactkey.png
	-$(RMDIR) .gle