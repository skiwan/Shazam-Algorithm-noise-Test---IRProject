for filename in querries/10/*; do 
	python audfprint/audfprint.py match --dbase audfprint/fulldbase.pklz "$filename"	
done