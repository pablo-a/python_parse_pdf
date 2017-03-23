itera=1;

for file in $(ls PDF2017/)
	do
		test="text2017/"$file".txt"
		pdftotext -layout PDF2017/$file $test
		let itera++
	done
