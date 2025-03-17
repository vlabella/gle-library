all: circuit1.eps circuit1.pdf circuit1.png

circuit1.eps: circuit1.gle
	gle /device EPS /cairo circuit1.gle

circuit1.pdf: circuit1.gle
	gle /device PDF /cairo circuit1.gle

circuit1.png: circuit1.gle
	gle /device PNG /cairo /DPI 150 circuit1.gle

clean:
	-del circuit1.eps circuit1.pdf circuit1.png
	-rmdir /SQ .gle