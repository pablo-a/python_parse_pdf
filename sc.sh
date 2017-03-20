itera=1;

for file in $( ls PDFs)
	do
		test="text_version/Rungis2015_"$itera".txt"
		pdftotext -layout PDFs/$file $test
		let itera++
	done
