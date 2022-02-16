import requests,json,csv


mission_url = 'https://api.ei.mikit.app/mission_reward_count.json'
mission_dict = requests.get(mission_url).json()

headers = ['rocket','length','stars','reward','tier','rarity','count','seen','prop']

with open('Mission Props (NEW).csv','w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(headers)
    for r in mission_dict.keys():
        for l in mission_dict[r].keys():
            for s in mission_dict[r][l].keys():
                for c in mission_dict[r][l][s].keys():
                    if c == 'count':
                        count=mission_dict[r][l][s][c]
                    else:
                        for rw in mission_dict[r][l][s][c].keys():
                            for t in mission_dict[r][l][s][c][rw].keys():
                                for rt in mission_dict[r][l][s][c][rw][t].keys():
                                    prop=mission_dict[r][l][s][c][rw][t][rt]/count
                                    seen=mission_dict[r][l][s][c][rw][t][rt]
                                    if l == 'long':
                                        length = 'standard'
                                    elif l =='epic':
                                        length = 'extended'
                                    else:
                                        length = l
                                    if t == '0':
                                        tier='T1'
                                    elif t == '1':
                                        tier='T2'
                                    elif t == '2':
                                        tier='T3'
                                    else:
                                        tier='T4'
                                    row=(r,length,s,rw,tier,rt,count,seen,prop)
                                    csvwriter.writerow(row)


print("done")

