# Calculate levenstein distance between 2 strings returns an integer
def distance(s1, s2):
        m = len(s1) + 1
        n = len(s2) + 1
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
            
        for i in range(1, m):
            for j in range(1, n):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    
        return dp[m-1][n-1]

while True:
    query = input("Word to find > ")

    suggestions = []
    words = []

    # Increment to increase tolerance and decrease relevancy
    distance_max = 1

    # Retrieve words from txt file
    with open("words.txt") as f:
        words = f.read().split('\n')

    for x in words:
        if distance(query.lower(), x.lower()) <= distance_max:
            suggestions.append(x)

    if len(suggestions):
        print("Suggestions :")
        for x in suggestions:
            print(f'\t{x}')
    else:
        print("No suggestions!")

    print(f"{len(suggestions)} Found.")
