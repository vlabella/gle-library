all: fruitbar.eps fruitbar.pdf fruitbar.png

fruitbar.eps: fruitbar.gle
	gle /device EPS /cairo fruitbar.gle

fruitbar.pdf: fruitbar.gle
	gle /device PDF /cairo fruitbar.gle

fruitbar.png: fruitbar.gle
	gle /device PNG /cairo /DPI 150 fruitbar.gle

clean:
	-del fruitbar.eps fruitbar.pdf fruitbar.png
	-rmdir /SQ .gle