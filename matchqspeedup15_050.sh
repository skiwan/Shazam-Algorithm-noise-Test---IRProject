for filename in querries/speedUp15/0_5/*; do 
	python audfprint/audfprint.py match --dbase audfprint/fulldbase.pklz "$filename"	
done