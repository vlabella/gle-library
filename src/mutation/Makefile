all: mutation.eps mutation.pdf mutation.png

mutation.eps: mutation.gle
	gle /device EPS /cairo mutation.gle

mutation.pdf: mutation.gle
	gle /device PDF /cairo mutation.gle

mutation.png: mutation.gle
	gle /device PNG /cairo /DPI 150 mutation.gle

clean:
	-del mutation.eps mutation.pdf mutation.png
	-rmdir /SQ .gle