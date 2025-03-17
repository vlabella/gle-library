all: hubble.eps hubble.pdf hubble.png

hubble.eps: hubble.gle
	gle /device EPS /cairo hubble.gle

hubble.pdf: hubble.gle
	gle /device PDF /cairo hubble.gle

hubble.png: hubble.gle
	gle /device PNG /cairo /DPI 150 hubble.gle

clean:
	-del hubble.eps hubble.pdf hubble.png
	-rmdir /SQ .gle