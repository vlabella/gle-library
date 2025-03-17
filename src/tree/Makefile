all: tree.eps tree.pdf tree.png

tree.eps: tree.gle
	gle /device EPS /cairo tree.gle

tree.pdf: tree.gle
	gle /device PDF /cairo tree.gle

tree.png: tree.gle
	gle /device PNG /cairo /DPI 150 tree.gle

clean:
	-del tree.eps tree.pdf tree.png
	-rmdir /SQ .gle