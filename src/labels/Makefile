all: labels.eps labels.pdf labels.png

labels.eps: labels.gle
	gle /device EPS /cairo labels.gle

labels.pdf: labels.gle
	gle /device PDF /cairo labels.gle

labels.png: labels.gle
	gle /device PNG /cairo /DPI 150 labels.gle

clean:
	-del labels.eps labels.pdf labels.png
	-rmdir /SQ .gle