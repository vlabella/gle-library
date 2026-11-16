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

all: perceptron.eps perceptron.pdf perceptron.png

perceptron.eps: perceptron.gle
	gle -device EPS  perceptron.gle

eps: perceptron.eps

perceptron.pdf: perceptron.gle
	gle -device PDF  perceptron.gle

pdf: perceptron.pdf

perceptron.png: perceptron.gle
	gle -device PNG -DPI 150 perceptron.gle

png: perceptron.png

clean:
	-$(RM) perceptron.eps perceptron.pdf perceptron.png
	-$(RMDIR) .gle