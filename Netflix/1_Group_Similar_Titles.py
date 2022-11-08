def group_titles(titles):
    res = {}
    for title in titles:
        count = [0] * 26
        for ch in title:
            index = ord(ch) - ord('a')
            count[index] += 1
        key = tuple(count)
        if key in res:
            res[key].append(title)
        else:
            res[key] = [title]
    return res.values()

titles = ["duel","dule","speed","spede","deul","cars"]
gt = list(group_titles(titles))
query = "spede"

# Searching for all titles
for g in gt:
    if query in g:
        print(g)
