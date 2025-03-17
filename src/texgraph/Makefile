all: texgraph.eps texgraph.pdf texgraph.png

texgraph.eps: texgraph.gle
	gle /device EPS /cairo texgraph.gle

texgraph.pdf: texgraph.gle
	gle /device PDF /cairo texgraph.gle

texgraph.png: texgraph.gle
	gle /device PNG /cairo /DPI 150 texgraph.gle

clean:
	-del texgraph.eps texgraph.pdf texgraph.png
	-rmdir /SQ .gle