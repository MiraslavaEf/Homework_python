def gen_ims(im, num):
    i = 1
    while i < num:
        yield im
        i += 1


ranger = gen_ims('Lev', 100)
ims = [y for y in ranger]
print(ims)