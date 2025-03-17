all: mandelbrot.eps mandelbrot.pdf mandelbrot.png

mandelbrot.eps: mandelbrot.gle
	gle /device EPS /cairo mandelbrot.gle

mandelbrot.pdf: mandelbrot.gle
	gle /device PDF /cairo mandelbrot.gle

mandelbrot.png: mandelbrot.gle
	gle /device PNG /cairo /DPI 150 mandelbrot.gle

clean:
	-del mandelbrot.eps mandelbrot.pdf mandelbrot.png
	-rmdir /SQ .gle