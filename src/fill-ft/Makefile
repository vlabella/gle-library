all: fill-ft.eps fill-ft.pdf fill-ft.png

fill-ft.eps: fill-ft.gle
	gle /device EPS /cairo fill-ft.gle

fill-ft.pdf: fill-ft.gle
	gle /device PDF /cairo fill-ft.gle

fill-ft.png: fill-ft.gle
	gle /device PNG /cairo /DPI 150 fill-ft.gle

clean:
	-del fill-ft.eps fill-ft.pdf fill-ft.png
	-rmdir /SQ .gle