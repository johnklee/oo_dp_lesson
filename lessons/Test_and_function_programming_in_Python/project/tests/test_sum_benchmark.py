from my_sum import sum

def test_sum_benchmark(benchmark):
  hundred_one_list = [1] * 100
  result = benchmark(sum, hundred_one_list)
  assert result == 100
