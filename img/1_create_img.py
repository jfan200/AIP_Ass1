import matplotlib.pyplot as plt


def generate_graph(data1, data2, n):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # 第一个子图：Solution graph
    axs[0].bar(data1.keys(), data1.values())
    axs[0].set_title('Solution length in different layouts')
    axs[0].set_xlabel('Pacman Layout')
    axs[0].set_ylabel('Solution length')
    for i, v in enumerate(data1.values()):
        axs[0].text(i, v + 1, str(v), ha='center', va='bottom')

    # 第二个子图：Expanded graph
    axs[1].bar(data2.keys(), data2.values())
    axs[1].set_title('Expanded node size in different layouts')
    axs[1].set_xlabel('Pacman Layout')
    axs[1].set_ylabel('Expanded node size')
    for i, v in enumerate(data2.values()):
        axs[1].text(i, v + 1, str(v), ha='center', va='bottom')

    # 调整子图之间的水平间距
    plt.subplots_adjust(wspace=0.4)

    # 保存和显示图像
    plt.savefig(f'{n}_graph.png')
    plt.show()


# solution graph
solu_data1 = {
    'p1local': 14,
    'smallEHC': 18,
    'mediumMaze': 76,
    'TrapForGreedy': 117,
}

# expanded graph
expanded_data1 = {
    'p1local': 16,
    'smallEHC': 23,
    'mediumMaze': 151,
    'TrapForGreedy': 250
}

generate_graph(solu_data1, expanded_data1, 1)


# solution graph
solu_data2 = {
    'smallMaze': 19,
    'mediumMaze2': 68,
    'bigOpenMaze2': 138

}

# expanded graph
expanded_data2 = {
    'smallMaze': 16,
    'mediumMaze2': 197,
    'bigOpenMaze2': 3484
}

generate_graph(solu_data2, expanded_data2, 2)


# solution graph
solu_data3 = {
    'trickySearch': 60,
    'mediumCorners1': 88
}

# expanded graph
expanded_data3 = {
    'trickySearch': 40034,
    'mediumCorners1': 131958
}

generate_graph(solu_data3, expanded_data3, 3)
