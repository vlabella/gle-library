all: clip-ft.eps clip-ft.pdf clip-ft.png

clip-ft.eps: clip-ft.gle
	gle /device EPS /cairo clip-ft.gle

clip-ft.pdf: clip-ft.gle
	gle /device PDF /cairo clip-ft.gle

clip-ft.png: clip-ft.gle
	gle /device PNG /cairo /DPI 150 clip-ft.gle

clean:
	-del clip-ft.eps clip-ft.pdf clip-ft.png
	-rmdir /SQ .gle