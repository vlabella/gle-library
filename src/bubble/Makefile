all: bubble.eps bubble.pdf bubble.png

bubble.eps: bubble.gle
	gle /device EPS /cairo bubble.gle

bubble.pdf: bubble.gle
	gle /device PDF /cairo bubble.gle

bubble.png: bubble.gle
	gle /device PNG /cairo /DPI 150 bubble.gle

clean:
	-del bubble.eps bubble.pdf bubble.png
	-rmdir /SQ .gle