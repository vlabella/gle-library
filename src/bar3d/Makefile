all: bar3d.eps bar3d.pdf bar3d.png

bar3d.eps: bar3d.gle
	gle /device EPS /cairo bar3d.gle

bar3d.pdf: bar3d.gle
	gle /device PDF /cairo bar3d.gle

bar3d.png: bar3d.gle
	gle /device PNG /cairo /DPI 150 bar3d.gle

clean:
	-del bar3d.eps bar3d.pdf bar3d.png
	-rmdir /SQ .gle