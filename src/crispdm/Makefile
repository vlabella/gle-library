all: crispdm.eps crispdm.pdf crispdm.png

crispdm.eps: crispdm.gle
	gle /device EPS /cairo crispdm.gle

crispdm.pdf: crispdm.gle
	gle /device PDF /cairo crispdm.gle

crispdm.png: crispdm.gle
	gle /device PNG /cairo /DPI 150 crispdm.gle

clean:
	-del crispdm.eps crispdm.pdf crispdm.png
	-rmdir /SQ .gle