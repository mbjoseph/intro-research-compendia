
all: paper/report.pdf

data/raw/data.csv: analysis/01-get_data.py
	python analysis/01-get_data.py

data/clean/data_clean.csv: data/raw/data.csv analysis/02-clean_data.py
	python analysis/02-clean_data.py

figures/awesome_plot.png: data/clean/data_clean.csv analysis/03-eda.py
	python analysis/03-eda.py

paper/report.pdf: paper/report.md figures/awesome_plot.png
	pandoc paper/report.md -o paper/report.pdf

clean:
	rm -f paper/report.pdf
	rm -f figures/*.png
	rm -f data/clean/*.csv
	rm -f data/raw/*.csv
