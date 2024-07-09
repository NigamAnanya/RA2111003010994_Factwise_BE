def maxScore(cardPoints, k):
  n = len(cardPoints)
  current_sum = sum(cardPoints[:k])
  max_sum = current_sum

  for i in range(1, k + 1):
    current_sum += cardPoints[-i] - cardPoints[k - i]
    max_sum = max(max_sum, current_sum)

  return max_sum

cardPoints = list(map(int, input("CardPoints = ").split()))
k = int(input("k = "))

result = maxScore(cardPoints, k)
print(result)