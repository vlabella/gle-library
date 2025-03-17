all: lnx.eps lnx.pdf lnx.png

lnx.eps: lnx.gle
	gle /device EPS /cairo lnx.gle

lnx.pdf: lnx.gle
	gle /device PDF /cairo lnx.gle

lnx.png: lnx.gle
	gle /device PNG /cairo /DPI 150 lnx.gle

clean:
	-del lnx.eps lnx.pdf lnx.png
	-rmdir /SQ .gle