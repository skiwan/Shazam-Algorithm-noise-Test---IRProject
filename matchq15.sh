for filename in querries/15/*; do 
	python audfprint/audfprint.py match --dbase audfprint/fulldbase.pklz "$filename"	
done