for i in range(2,20):
    with open(f"multiplication.txt{i}","w") as f :
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}\n")
    break