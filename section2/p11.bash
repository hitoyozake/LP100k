
# sedはエスケープシーケンスなどをそのままでは扱えないので$を使って事前に展開する
cat hightemp.txt | sed -e s/$'\t'/$' '/g

# タブ区切りファイルの表示
expand -i hightemp.txt

tr "\t" " " < hightemp.txt > out.txt
