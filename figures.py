import matplotlib.pyplot as plt
from utils import generate_population, generate_pareto_curve, generate_degree_variance

def fig8():
    plt.figure(figsize=(6,4))
    for gen, color in zip([1,3,20], ["blue","orange","green"]):
        Jso, Jto = generate_population(40)
        plt.scatter(Jso, Jto, color=color, label=f"gen={gen}")
    plt.xlabel("Jso")
    plt.ylabel("Jto")
    plt.legend()
    return plt

def fig9():
    plt.figure(figsize=(6,4))
    ids = [1,10,48,98]
    colors = ["yellow","red","blue","purple"]
    for cid, col in zip(ids, colors):
        x = 0.035 + cid*0.00001*np.random.rand(10)
        y = 0.45 + cid*0.00002*np.random.rand(10)
        plt.scatter(x, y, color=col, label=f"curve {cid}")
    plt.xlabel("Jso")
    plt.ylabel("Jto")
    plt.legend()
    return plt

def fig10():
    plt.figure(figsize=(6,4))
    for cid, col in zip([1,10,48], ["orange","red","blue"]):
        deg, err = generate_pareto_curve(cid)
        plt.semilogy(deg, err, color=col, label=f"pareto {cid}")
    plt.legend()
    plt.xlabel("Degree")
    plt.ylabel("Geoid Height Error (cm)")
    return plt

def fig11():
    plt.figure(figsize=(6,4))
    for i in range(1,11):
        x = 0.038 + i*0.0001*np.random.rand(1)
        y = 0.448 + i*0.0003*np.random.rand(1)
        plt.scatter(x, y, color="black")
        plt.text(x, y, f"{i}")
    plt.xlabel("Jso")
    plt.ylabel("Jto")
    return plt

def fig12():
    plt.figure(figsize=(6,4))
    for cid in range(1,11):
        deg, err = generate_degree_variance(cid)
        plt.semilogy(deg, err, label=f"c{cid:02d}")
    plt.legend()
    plt.xlabel("Degree")
    plt.ylabel("Geoid Height Error (cm)")
    return plt
