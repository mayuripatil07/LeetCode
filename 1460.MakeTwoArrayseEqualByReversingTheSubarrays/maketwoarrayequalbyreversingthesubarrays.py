 i = 0
        while(i < len(arr)):
            if arr[i] != target[i]:
                for j in range(i,len(arr)):
                    if arr[j] == target[i]:
                        arr[i:j+1] = arr[i:j+1][::-1]
                        break
                    else:
                        continue
            i += 1


        if target == arr:
            return True
        return False
       
