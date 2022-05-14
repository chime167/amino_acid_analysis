# Final_Project

* ABOUT *

This is a front-end amino acid attribute analysis web program.
It is a fast and simple to use interface that provides a table of info for each sequence and stores the results in a database.
Each table contains a count of each of the 20 amino acids found in each entered sequence, as well as the length, weight, pI, hydrophobicity, instability index, and the FASTA Accession ID.

It utilizes:
    Python/Biopython
    CGI(via Python)
    Javascript/jQuery
    HTML/CSS
    MySQL

It aims to be an accessible and facilitate the use of the Biopython package, while also allowing swift data entry and graphical access to a database.

* REQUIREMENTS *

CPU: The program is fairly lightweight and at least 1GB of memory is recommended.
Browser: It was tested as functioning in chromium based browsers, as well as Firefox and its derivatives.
Database: It is intended to be used with MySQL, so access to a MySQL database is necessary to store results.

* USAGE *

1. Paste amino acid sequences that are in FASTA format into the text area. Multiple entries can be pasted.
2. Click 'Submit'. Results will appear in a table without the page refreshing.
3. Click 'Show database' to be connected to the MySQL database, where the results of all previous runs are stored and    displayed in another table.



