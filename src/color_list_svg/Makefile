all: color_list_svg.eps color_list_svg.pdf color_list_svg.png

color_list_svg.eps: color_list_svg.gle
	gle /device EPS /cairo color_list_svg.gle

color_list_svg.pdf: color_list_svg.gle
	gle /device PDF /cairo color_list_svg.gle

color_list_svg.png: color_list_svg.gle
	gle /device PNG /cairo /DPI 150 color_list_svg.gle

clean:
	-del color_list_svg.eps color_list_svg.pdf color_list_svg.png
	-rmdir /SQ .gle