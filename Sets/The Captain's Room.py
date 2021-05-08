K = int(input())
roomList = list(map(int,input().split(' ')))
roomSet = set(roomList) 
sumRoomSet = sum(roomSet)
sumRoomList = sum(roomList)
temp = sumRoomSet * K - sumRoomList 
answer = temp / (K - 1) 
print(int(answer))
