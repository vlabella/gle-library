all: circuit2.eps circuit2.pdf circuit2.png

circuit2.eps: circuit2.gle
	gle /device EPS /cairo circuit2.gle

circuit2.pdf: circuit2.gle
	gle /device PDF /cairo circuit2.gle

circuit2.png: circuit2.gle
	gle /device PNG /cairo /DPI 150 circuit2.gle

clean:
	-del circuit2.eps circuit2.pdf circuit2.png
	-rmdir /SQ .gle