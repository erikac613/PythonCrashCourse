favorite_places = {'liz': ['hawaii', 'germany'], 'erika': ['new zealand', 'canada'], 'george': ['scotland'], 'sarah': ['france', 'san francisco', 'bermuda']}

for name, places in favorite_places.items():
    if len(places) >= 2:
        print("\n" + name.title() + "'s favorite places are:")
    else:
        print("\n" + name.title() + "'s favorite place is:")
    for place in places:
        print("\t" + place.title())
