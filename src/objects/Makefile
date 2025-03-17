all: objects.eps objects.pdf objects.png

objects.eps: objects.gle
	gle /device EPS /cairo objects.gle

objects.pdf: objects.gle
	gle /device PDF /cairo objects.gle

objects.png: objects.gle
	gle /device PNG /cairo /DPI 150 objects.gle

clean:
	-del objects.eps objects.pdf objects.png
	-rmdir /SQ .gle