all: opening.eps opening.pdf opening.png

opening.eps: opening.gle
	gle /device EPS /cairo opening.gle

opening.pdf: opening.gle
	gle /device PDF /cairo opening.gle

opening.png: opening.gle
	gle /device PNG /cairo /DPI 150 opening.gle

clean:
	-del opening.eps opening.pdf opening.png
	-rmdir /SQ .gle