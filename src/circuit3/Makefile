all: circuit3.eps circuit3.pdf circuit3.png

circuit3.eps: circuit3.gle
	gle /device EPS /cairo circuit3.gle

circuit3.pdf: circuit3.gle
	gle /device PDF /cairo circuit3.gle

circuit3.png: circuit3.gle
	gle /device PNG /cairo /DPI 150 circuit3.gle

clean:
	-del circuit3.eps circuit3.pdf circuit3.png
	-rmdir /SQ .gle