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

all: business_cards_10_per_A4.eps business_cards_10_per_A4.pdf business_cards_10_per_A4.png

business_cards_10_per_A4.eps: business_cards_10_per_A4.gle
	gle -device EPS -cairo business_cards_10_per_A4.gle

business_cards_10_per_A4.pdf: business_cards_10_per_A4.gle
	gle -device PDF -cairo business_cards_10_per_A4.gle

business_cards_10_per_A4.png: business_cards_10_per_A4.gle
	gle -device PNG -cairo -DPI 150 business_cards_10_per_A4.gle

clean:
	-$(RM) business_cards_10_per_A4.eps business_cards_10_per_A4.pdf business_cards_10_per_A4.png
	-$(RMDIR) .gle