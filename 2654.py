n = input()
nams = []
pods = []
mats = []
matds = []

for nIndex in range(n):
    nam, pod, mat, matd = raw_input().split(' ')
    nams.insert(len(nams), nam)
    pods.insert(len(pods), int(pod))
    mats.insert(len(mats), int(mat))
    matds.insert(len(matds), int(matd))

## pods
maior = 0

for pod in pods:
    if pod > maior:
        maior = pod

remNams = []
remPods = []
remMats = []
remMatds = []
 
for i in range(len(pods)):
    if pods[i] == maior:
        remNams.insert(len(remNams), nams[i])
        remPods.insert(len(remPods), pods[i])
        remMats.insert(len(remMats), mats[i])
        remMatds.insert(len(remMatds), matds[i])

nams = remNams
pods = remPods
mats = remMats
matds = remMatds 

if len(nams) == 1:
    print nams[0]
else:
    ## mats
    maior = 0

    for mat in mats:
        if mat > maior:
            maior = mat

    remNams = []
    remPods = []
    remMats = []
    remMatds = []
    
    for i in range(len(mats)):
        if mats[i] == maior:
            remNams.insert(len(remNams), nams[i])
            remPods.insert(len(remPods), pods[i])
            remMats.insert(len(remMats), mats[i])
            remMatds.insert(len(remMatds), matds[i])

    nams = remNams
    pods = remPods
    mats = remMats
    matds = remMatds

    if len(nams) == 1:
        print nams[0]
    else:
        ## matds
        menor = 101

        for matd in matds:
            if matd < menor:
                menor = matd

        remNams = []
        remPods = []
        remMats = []
        remMatds = []
        
        for i in range(len(matds)):
            if matds[i] == menor:
                remNams.insert(len(remNams), nams[i])
                remPods.insert(len(remPods), pods[i])
                remMats.insert(len(remMats), mats[i])
                remMatds.insert(len(remMatds), matds[i])

        nams = remNams
        pods = remPods
        mats = remMats
        matds = remMatds

        if len(nams) == 1:
            print nams[0]
        else:
            nams = sorted(nams)
            print nams[0]