all: seaborn.eps seaborn.pdf seaborn.png

seaborn.eps: seaborn.gle
	gle /device EPS /cairo seaborn.gle

seaborn.pdf: seaborn.gle
	gle /device PDF /cairo seaborn.gle

seaborn.png: seaborn.gle
	gle /device PNG /cairo /DPI 150 seaborn.gle

clean:
	-del seaborn.eps seaborn.pdf seaborn.png
	-rmdir /SQ .gle