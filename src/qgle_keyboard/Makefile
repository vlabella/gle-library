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

all: qgle_keyboard.eps qgle_keyboard.pdf qgle_keyboard.png

qgle_keyboard.eps: qgle_keyboard.gle
	gle -device EPS -cairo qgle_keyboard.gle

qgle_keyboard.pdf: qgle_keyboard.gle
	gle -device PDF -cairo qgle_keyboard.gle

qgle_keyboard.png: qgle_keyboard.gle
	gle -device PNG -cairo -DPI 150 qgle_keyboard.gle

clean:
	-$(RM) qgle_keyboard.eps qgle_keyboard.pdf qgle_keyboard.png
	-$(RMDIR) .gle