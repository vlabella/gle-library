all: house.eps house.pdf house.png

house.eps: house.gle
	gle /device EPS /cairo house.gle

house.pdf: house.gle
	gle /device PDF /cairo house.gle

house.png: house.gle
	gle /device PNG /cairo /DPI 150 house.gle

clean:
	-del house.eps house.pdf house.png
	-rmdir /SQ .gle