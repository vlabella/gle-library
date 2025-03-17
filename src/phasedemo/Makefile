all: phasedemo.eps phasedemo.pdf phasedemo.png

phasedemo.eps: phasedemo.gle
	gle /device EPS /cairo phasedemo.gle

phasedemo.pdf: phasedemo.gle
	gle /device PDF /cairo phasedemo.gle

phasedemo.png: phasedemo.gle
	gle /device PNG /cairo /DPI 150 phasedemo.gle

clean:
	-del phasedemo.eps phasedemo.pdf phasedemo.png
	-rmdir /SQ .gle