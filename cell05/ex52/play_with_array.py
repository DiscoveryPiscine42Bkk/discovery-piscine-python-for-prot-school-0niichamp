import heapq

nums = [2, 8, 9, 48, 8, 22, -12, 2]
plus_nums = [x + 2 for x in nums]
great_pnum = heapq.nlargest(5, plus_nums)
list_great_pnums = [x for x in plus_nums if x in great_pnum]
print(list_great_pnums)