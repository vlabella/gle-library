all: perceptron.eps perceptron.pdf perceptron.png

perceptron.eps: perceptron.gle
	gle /device EPS /cairo perceptron.gle

perceptron.pdf: perceptron.gle
	gle /device PDF /cairo perceptron.gle

perceptron.png: perceptron.gle
	gle /device PNG /cairo /DPI 150 perceptron.gle

clean:
	-del perceptron.eps perceptron.pdf perceptron.png
	-rmdir /SQ .gle