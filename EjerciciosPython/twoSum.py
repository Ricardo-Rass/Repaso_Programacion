def twosum(nums,target):
    #hashmap donde se guardaran los valores
    hashMap = {}
    #recorre el indice y el valor.  Se necesita el enumerate()  ya que de lo contrario marca error porque no se podra iterar
    for index, valor in enumerate(nums):
        diferencia = target - valor
        #si esta en el hashmap
        if diferencia in hashMap:
            #retorna el indice del valor de la diferencia que se guardo en el hashmap y el indice del valor donde se hizo la resta 
            return [hashMap[diferencia], index]
        #si no esta en el hashmap
        hashMap[valor]=index  



print(twosum([1,2,3],4))




#opcion 2
def twoSum( nums, int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

print(twosum([1,2,3],3))                