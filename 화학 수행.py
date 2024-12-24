import matplotlib.pyplot as plt
import numpy as np
import random


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  

choice = input("반응물을 선택하세요 (1: NaOH, 2: Mg(OH)2): ")
concentration = random.uniform(0.01, 20.00)

volume = 1 
hcl_concentration = 1.0  

if choice == "1":  
    substance = "NaOH"
    moles = concentration * volume  
    water_moles = moles  
elif choice == "2":  
    substance = "Mg(OH)2"
    moles = concentration * volume  
    water_moles = moles * 2  

print(f"{substance}의 랜덤 몰 농도: {concentration:.2f}M")


substances = ['나트륨(Na+)', '마그네슘(Mg2+)', '물(H2O)']
moles_arr = [0, 0, water_moles]  
if choice == "1":
    moles_arr[0] = moles 
elif choice == "2":
    moles_arr[1] = moles  

plt.figure(figsize=(10, 6))
plt.bar(substances, moles_arr, color=['blue', 'orange', 'cyan'])
plt.xlabel('물질')
plt.ylabel('몰 수')
plt.title('반응 후 구경꾼 이온과 물의 몰 수')
plt.ylim(0, max(moles_arr) * 1.2) 
plt.show()

required_hcl_volume = moles if choice == "1" else moles*2
print(f"완전 중화를 위해 필요한 1M HCl 용액의 양: {required_hcl_volume:.2f}L")
