for filename in querries/speech10/-5/*; do 
	python audfprint/audfprint.py match --dbase audfprint/fulldbase.pklz "$filename"	
done