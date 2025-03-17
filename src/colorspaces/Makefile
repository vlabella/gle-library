all: colorspaces.eps colorspaces.pdf colorspaces.png

colorspaces.eps: colorspaces.gle
	gle /device EPS /cairo colorspaces.gle

colorspaces.pdf: colorspaces.gle
	gle /device PDF /cairo colorspaces.gle

colorspaces.png: colorspaces.gle
	gle /device PNG /cairo /DPI 150 colorspaces.gle

clean:
	-del colorspaces.eps colorspaces.pdf colorspaces.png
	-rmdir /SQ .gle