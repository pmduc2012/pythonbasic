import random
random.SystemRandom()

TM = ['tm1','tm2','tm3']
HV = ['hv1','hv2','hv3','hv4','hv5','hv6','hv7','hv8','hv9','hv10']
TV = ['tv1','tv2','tv3','tv4','tv5','tv6','tv7','tv8','tv9']
TD = ['td1','td2','td3']
DH = []

random.sample(TM,1)
DH.append(random.sample(TM,1))
random.sample(HV,4)
DH.append(random.sample(HV,4))
random.sample(TV,4)
DH.append(random.sample(TV,4))
random.sample(TD,2)
DH.append(random.sample(TD,1))
print(DH)