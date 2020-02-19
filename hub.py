with open("./a_example.in", "r") as f:
    # Data Ingestion
    m, n, s = 0, 0, []
    line = 0
    m, n = f.readline().split(' ')
    m, n = int(m), int(n)
    s = f.readline()[:-1].split(' ')
    s = [int(i) for i in s]

    # Data Crunching
    
