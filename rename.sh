#usage ./rename.sh $1

for f in *
do
  mv $f $f.$1
done
