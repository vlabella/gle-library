all: elliptical_arcs.eps elliptical_arcs.pdf elliptical_arcs.png

elliptical_arcs.eps: elliptical_arcs.gle
	gle /device EPS /cairo elliptical_arcs.gle

elliptical_arcs.pdf: elliptical_arcs.gle
	gle /device PDF /cairo elliptical_arcs.gle

elliptical_arcs.png: elliptical_arcs.gle
	gle /device PNG /cairo /DPI 150 elliptical_arcs.gle

clean:
	-del elliptical_arcs.eps elliptical_arcs.pdf elliptical_arcs.png
	-rmdir /SQ .gle