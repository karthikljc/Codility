print("### For Loop ###")

anime_arr = ["Code Geass","Cowboy Bebop","Naruto","Blood+","GIS"]

for anime in anime_arr :
  print(anime)

print("\n")
print("### For Using Indexes ###")

for i in range(len(anime_arr)) :
  print("i :"+str(i)+" anime:"+anime_arr[i])
