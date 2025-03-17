all: circuit4.eps circuit4.pdf circuit4.png

circuit4.eps: circuit4.gle
	gle /device EPS /cairo circuit4.gle

circuit4.pdf: circuit4.gle
	gle /device PDF /cairo circuit4.gle

circuit4.png: circuit4.gle
	gle /device PNG /cairo /DPI 150 circuit4.gle

clean:
	-del circuit4.eps circuit4.pdf circuit4.png
	-rmdir /SQ .gle