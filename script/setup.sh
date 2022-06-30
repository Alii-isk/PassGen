#!/bin/bash

mkdir wordlists
cd wordlists
wget" https://sec.stanev.org/dict/used.txt.gz" -o list-1.gz
wget "https://sec.stanev.org/dict/insidepro.txt.gz" -o list-2.gz
wget "https://wpa-sec.stanev.org/dict/cracked.txt.gz" -o list-3.gz
wget "https://sec.stanev.org/dict/cow.txt.gz" -o list-4.gz
wget "https://sec.stanev.org/dict/old_gold.txt.gz" -o list-5.gz
wget "https://sec.stanev.org/dict/wp.txt.gz" -o list-6.gz
python default.py -o list-7


for i in {1..6}
do
   gzip -d "list-$i.gz"
done

for i in *.txt;
   do cat $i >> default.txt;
done


#tar cvzf file.tar.gz *.txt
#tar xvzf file.tar.gz -C /path/to/parent/dir

#generate all > gzip it




