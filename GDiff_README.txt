1. Generate ctags for all the files in the software application
	ctags -RV -x --c-types=f * > gdiff_tags

2. Run parse_ctags.py
	a. Extract all the main() functions from gdiff_tags
	b. Concatinate main() with its file name, as there can be many main() functions in the application.
	c. Also create a list of all files containing the main() function.  (To be used by cflow) 
	d. Find all the '.c' files in the application (all including in different folders)
		Examples:
			find ./ -type f -name "*.c" > find_output
			find ./server/ -type f -name '*.c' -printf '%u,%p\n
			find ./server/ -type f -name '*.c' -exec bash -c 'n="${1%/*}"; n="${n##*/}"; echo "$n",$1' _ {} \;

	e. Run 'cflow' with each files that has main() function, add all other files as arguments ???
	f. Write result to a file. 
