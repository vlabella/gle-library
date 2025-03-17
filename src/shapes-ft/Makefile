all: shapes-ft.eps shapes-ft.pdf shapes-ft.png

shapes-ft.eps: shapes-ft.gle
	gle /device EPS /cairo shapes-ft.gle

shapes-ft.pdf: shapes-ft.gle
	gle /device PDF /cairo shapes-ft.gle

shapes-ft.png: shapes-ft.gle
	gle /device PNG /cairo /DPI 150 shapes-ft.gle

clean:
	-del shapes-ft.eps shapes-ft.pdf shapes-ft.png
	-rmdir /SQ .gle