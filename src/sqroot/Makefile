all: sqroot.eps sqroot.pdf sqroot.png

sqroot.eps: sqroot.gle
	gle /device EPS /cairo sqroot.gle

sqroot.pdf: sqroot.gle
	gle /device PDF /cairo sqroot.gle

sqroot.png: sqroot.gle
	gle /device PNG /cairo /DPI 150 sqroot.gle

clean:
	-del sqroot.eps sqroot.pdf sqroot.png
	-rmdir /SQ .gle