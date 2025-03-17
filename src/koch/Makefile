all: koch.eps koch.pdf koch.png

koch.eps: koch.gle
	gle /device EPS /cairo koch.gle

koch.pdf: koch.gle
	gle /device PDF /cairo koch.gle

koch.png: koch.gle
	gle /device PNG /cairo /DPI 150 koch.gle

clean:
	-del koch.eps koch.pdf koch.png
	-rmdir /SQ .gle