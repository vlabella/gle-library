all: boxplot-ft.eps boxplot-ft.pdf boxplot-ft.png

boxplot-ft.eps: boxplot-ft.gle
	gle /device EPS /cairo boxplot-ft.gle

boxplot-ft.pdf: boxplot-ft.gle
	gle /device PDF /cairo boxplot-ft.gle

boxplot-ft.png: boxplot-ft.gle
	gle /device PNG /cairo /DPI 150 boxplot-ft.gle

clean:
	-del boxplot-ft.eps boxplot-ft.pdf boxplot-ft.png
	-rmdir /SQ .gle