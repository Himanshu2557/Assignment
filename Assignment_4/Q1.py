print('--------------------Question-1---------------------')

# Creation function to print steps to transfer disc from A to C
def TowerOfHanoi(n,source,destination,helper):

    # Base Case
    if n==0:
        return
# Firstly moving n-1 disc to B using C
    TowerOfHanoi(n-1,source,helper,destination)

# Moving top disc from A to C
    print("Move top disc from \033[1m%s\033[0m to \033[1m%s\033[0m" %(source,destination))

# Moving n-1 disc from B TO C Using A
    TowerOfHanoi(n-1,helper,destination,source)


# calling Function For 3 Disc
TowerOfHanoi(3,'A','C','B')


