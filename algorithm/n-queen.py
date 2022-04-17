# backtracking with n-queen
# n = 2x2
# thuật toán quay lui
# số hàng : i, số cột: j, 
# đường chéo xuôi = đường chéo ngược = i + j- n
c = [0 for i in range(4)]
d1 = [0 for i in range(8)]
d2 = [0 for i in range(8)]
arr = [0 for i in range(4)]
def print_result():
	board=[[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		board[i][arr[i]] = 1
	for i in range(4):
		for j in range(4):
			print(board[i][j], end=" ")
		print('\n')

# print_arr(arr)
def backtrack(i):
	for j in range(4):
		if c[j] == 0 and d1[i - j +2] == 0 and d2[i + j - 1] == 0:
			arr[i] = j
			d1[i + j -2] =1
			d2[i + j -2]=1
			if i==3:
				print_result()
				print("-------")
			else: 
				backtrack(i+1)
			# backtrack
			c[j] = 0
			d1[i - j +2] = 0
			d1[i+j-1] = 0
backtrack(0)
