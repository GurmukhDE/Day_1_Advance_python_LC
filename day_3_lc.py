lis = [1,2,3,4,5]

new_lis = []

for j in lis:
    if j %2!=0:
        new_lis.append(j*2)

logger.info(new_lis)

new_lc = [j*2 for j in lis if  j % 2!=0 ]
logger.info(new_lc)
