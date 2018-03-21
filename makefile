rm sample_1_10.png
rm sample_1_100.png
rm sample_1_1000.png
rm sample_2_10.png
rm sample_2_100.png
rm sample_2_1000.png
rm sample_1_10.txt
rm sample_1_100.txt
rm sample_1_1000.txt
rm sample_2_10.txt
rm sample_2_100.txt
rm sample_2_1000.txt

sample_1_10.png: SantiagoGomez_analysis.py sample_1_10.txt
	python SantiagoGomez_analysis.py

sample_1_10.txt: SantiagoGomez_generar.py
	python SantiagoGomez_generar.py

