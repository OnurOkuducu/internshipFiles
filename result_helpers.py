lastTen = []

def most_common(lst):
    return max(set(lst), key=lst.count)

def scoreKeeper(currentEmo):
    if currentEmo == 'empty':
        if lastTen == []:
            return "No"
        return most_common(lastTen)
    if len(lastTen) < 5:
        lastTen.append(currentEmo)
    else:
        lastTen.pop(0)
        lastTen.append(currentEmo)
    print(lastTen)
    return most_common(lastTen)

def apply_threshold(score,threshold):
    if score>1:
        score = score/100
    
    if score >=threshold:
        return True
    
    return False