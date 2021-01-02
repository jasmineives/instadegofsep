import config
from instapy import InstaPy
from instapy.util import smart_run

session = InstaPy(username=config.username,
                  password=config.password,
                  headless_browser=False)


def sortFollowers(mutualsList):
    mutualsDict = dict()
    for mutual in mutualsList:
        mutualsDict[mutual] = len(session.grab_followers(username = mutual,
                                                         amount="full",
                                                         live_match=True,
                                                         store_locally=False))
                                                        
    print(mutualsList)
    print(mutualsDict)
    quickSort(mutualsList, mutualsDict, 0, 1)
    print(mutualsList)
    print(mutualsDict)
    

    return mutualsList


def quickSort(arr, dic, low,high):
    # [ 8 2 9 8 9 5 3 7]
    if high == -1:
        high = len(arr) - 1
    if(low < high):
        pIndex = partition(arr, dic, low, high)
        
        quickSort(arr, dic, low, pIndex - 1)
        quickSort(arr, dic, pIndex + 1, high)

def partition(arr,dic, low, high):
    i = low - 1
    pivot = dic[arr[high]]
    for j in range(low, high - 1):
        if dic[arr[j]] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        
    arr[i + 1],arr[high] = arr[high],arr[i + 1]
    return i + 1


with smart_run(session):
    mutualsList = session.pick_mutual_following(username= config.username,
                                live_match=False,
                                store_locally=False)
    sortFollowers(mutualsList)
