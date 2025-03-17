all: clip.eps clip.pdf clip.png

clip.eps: clip.gle
	gle /device EPS /cairo clip.gle

clip.pdf: clip.gle
	gle /device PDF /cairo clip.gle

clip.png: clip.gle
	gle /device PNG /cairo /DPI 150 clip.gle

clean:
	-del clip.eps clip.pdf clip.png
	-rmdir /SQ .gle