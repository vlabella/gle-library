all: wallx.eps wallx.pdf wallx.png

wallx.eps: wallx.gle
	gle /device EPS /cairo wallx.gle

wallx.pdf: wallx.gle
	gle /device PDF /cairo wallx.gle

wallx.png: wallx.gle
	gle /device PNG /cairo /DPI 150 wallx.gle

clean:
	-del wallx.eps wallx.pdf wallx.png
	-rmdir /SQ .gle