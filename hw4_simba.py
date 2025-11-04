def count_simba(list):
    count = 0
    for item in list:
        count += item.count("Simba")
    return count

list = ["Simba and Nala are lions.", 
              "I laugh in the face of danger.", 
              "Hakuna matata", 
              "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 

print(count_simba(list))