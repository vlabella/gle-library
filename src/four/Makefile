all: four.eps four.pdf four.png

four.eps: four.gle
	gle /device EPS /cairo four.gle

four.pdf: four.gle
	gle /device PDF /cairo four.gle

four.png: four.gle
	gle /device PNG /cairo /DPI 150 four.gle

clean:
	-del four.eps four.pdf four.png
	-rmdir /SQ .gle