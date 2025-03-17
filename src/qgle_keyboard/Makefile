all: qgle_keyboard.eps qgle_keyboard.pdf qgle_keyboard.png

qgle_keyboard.eps: qgle_keyboard.gle
	gle /device EPS /cairo qgle_keyboard.gle

qgle_keyboard.pdf: qgle_keyboard.gle
	gle /device PDF /cairo qgle_keyboard.gle

qgle_keyboard.png: qgle_keyboard.gle
	gle /device PNG /cairo /DPI 150 qgle_keyboard.gle

clean:
	-del qgle_keyboard.eps qgle_keyboard.pdf qgle_keyboard.png
	-rmdir /SQ .gle