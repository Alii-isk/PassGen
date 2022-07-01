wget "https://sec.stanev.org/dict/used.txt.gz" -o list-1.gz
wget "https://sec.stanev.org/dict/insidepro.txt.gz" -o list-2.gz
wget "https://wpa-sec.stanev.org/dict/cracked.txt.gz" -o list-3.gz
wget "https://sec.stanev.org/dict/cow.txt.gz" -o list-4.gz
wget "https://sec.stanev.org/dict/old_gold.txt.gz" -o list-5.gz
wget "https://sec.stanev.org/dict/wp.txt.gz" -o list-6.gz
python default.py -o list-7


gunzip *.gz

tar cvzf mylist.tar.gz *.txt

rm list-*
rm *.txt


#cat names-ar-1025.txt | while read line; do python main.py -o $line --extend $line; done


#!tar cvzf mylist.tar.gz *.txt
#tar xvzf file.tar.gz -C /path/to/parent/dir

#generate all > gzip it




