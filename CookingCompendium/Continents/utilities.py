def build_library(
    lib, topic_key, continent_key, country_key, state_key=None, recipes=None):
    # Create a key for the ingredient if it doesn't exist
    if lib.get(topic_key) is None:
        lib[topic_key] = {}

    # Create a key for the continent
    if lib[topic_key].get(continent_key) is None:
        if state_key is not None:
            lib[topic_key][continent_key] = {}
        else:
            lib[topic_key][continent_key] = []

    # Create a key for the country
    if state_key is not None:
        if country_key not in lib[topic_key][continent_key]:
            lib[topic_key][continent_key][country_key] = []
        lib[topic_key][continent_key][country_key].append((state_key, recipes))
    else:
        if country_key not in lib[topic_key][continent_key]:
            lib[topic_key][continent_key].append((country_key, recipes))


    return lib