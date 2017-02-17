
# Bash for( ) Doesn't work with float. Use seq command instead.
xmin=0.169
xmax=0.179
offs=0.001

echo Second

# ~/work/python/julia [517]-> for i in $(seq -1.9 0.1 -1.4); do echo $i; done

for i in $( seq $xmin $offs $xmax )
do
	echo $i
  	./argjcosZsq.py $i
done
