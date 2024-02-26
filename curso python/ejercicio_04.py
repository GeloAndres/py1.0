countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set = new_set.union(countries)
new_set = new_set.union(northAm)
new_set = new_set.union(centralAm)
new_set = new_set.union(southAm)


print(new_set)