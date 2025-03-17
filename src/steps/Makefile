all: steps.eps steps.pdf steps.png

steps.eps: steps.gle
	gle /device EPS /cairo steps.gle

steps.pdf: steps.gle
	gle /device PDF /cairo steps.gle

steps.png: steps.gle
	gle /device PNG /cairo /DPI 150 steps.gle

clean:
	-del steps.eps steps.pdf steps.png
	-rmdir /SQ .gle