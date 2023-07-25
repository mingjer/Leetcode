# test case
# startsAt = [1, 2]
# endsAt = [5, 4]
# output = [1, 1]

# test case
# startsAt = [3, 1, 5]
# endsAt = [3, 5, 6]
# output = [1, 2, 1]

startsAt = [2, 2, 1, 3]
endsAt = [4, 3, 1, 4]
output = [2, 2, 0, 2]


# startsAt = [4, 1, 1, 4, 3]
# endsAt = [7, 6, 1, 5, 4]
# output = [3, 4, 1, 3, 3]

# startsAt = [4, 6, 1, 5, 3]
# endsAt = [4, 6, 1, 5, 3]
# output = [0, 0, 0, 0, 0]


ans = [0] * len(startsAt)

intervals = []

for i in range(len(startsAt)):
    intervals.append([startsAt[i], endsAt[i]])

# create a hashMap {interval: original index}
hashMap = {}

for index, value in enumerate(intervals):
    hashMap[tuple(value)] = index

print("orginal intervals ", intervals)
# sort the invtervals by their start point
intervals.sort()

print("sorted intervals ", intervals)

for i in range(len(intervals)):
    for j in range(i + 1, len(intervals)):
        if intervals[j][0] <= intervals[i][1]:
            ans[hashMap[tuple(intervals[i])]] += 1
            ans[hashMap[tuple(intervals[j])]] += 1
        elif intervals[j][0] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
            ans[hashMap[tuple(intervals[i])]] += 1
            ans[hashMap[tuple(intervals[j])]] += 1


if output == ans:
    print("correct!!")
else:
    print("sb, cant even get this one right")
    print(output)
    print(ans)
    