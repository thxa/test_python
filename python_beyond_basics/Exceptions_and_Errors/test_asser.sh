echo "without -O"
python -m timeit -n 1 -s "from random import randrange; from sort_set import SortedSet; s = SortedSet(randrange(1000) for _ in range(2000))" "[s.count(i) for i in range(1000)]"

echo "with -O"
python -O -m timeit -n 1 -s "from random import randrange; from sort_set import SortedSet; s = SortedSet(randrange(1000) for _ in range(2000))" "[s.count(i) for i in range(1000)]"