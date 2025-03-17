all: pythagoras.eps pythagoras.pdf pythagoras.png

pythagoras.eps: pythagoras.gle
	gle /device EPS /cairo pythagoras.gle

pythagoras.pdf: pythagoras.gle
	gle /device PDF /cairo pythagoras.gle

pythagoras.png: pythagoras.gle
	gle /device PNG /cairo /DPI 150 pythagoras.gle

clean:
	-del pythagoras.eps pythagoras.pdf pythagoras.png
	-rmdir /SQ .gle