all: semitrans.eps semitrans.pdf semitrans.png

semitrans.eps: semitrans.gle
	gle /device EPS /cairo semitrans.gle

semitrans.pdf: semitrans.gle
	gle /device PDF /cairo semitrans.gle

semitrans.png: semitrans.gle
	gle /device PNG /cairo /DPI 150 semitrans.gle

clean:
	-del semitrans.eps semitrans.pdf semitrans.png
	-rmdir /SQ .gle