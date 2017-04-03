import xml.etree.cElementTree as ET
import pprint

def count_stuff(filename):
    # YOUR CODE HERE
    towns = dict()
    zip_codes = dict()
    streets = dict()
    keys = dict()

    bad_coords = []

    tree = ET.parse(filename)
    root = tree.getroot()

    for element in root.iter():
        tag = element.tag

        if tag == 'node':
            lat = float(element.attrib['lat'])
            lon = float(element.attrib['lon'])

            if not(40 < lat < 42 or -79 < lon < -81):
                print (lat,lon)

        if tag == 'tag':
            key = element.attrib['k']
            if key not in keys:
                keys[key] = 0

            keys[key] += 1

            if key == 'addr:city':
                city = element.attrib['v']

                if(city not in towns):
                    towns[city] = 0

                towns[city] += 1

            if key == 'addr:postcode':
                zip_code = element.attrib['v']

                if zip_code not in zip_codes:
                    zip_codes[zip_code] = 0

                zip_codes[zip_code] += 1

            if key == 'addr:street':
                street = element.attrib['v']

                if street not in streets:
                    streets[street] = 0

                streets[street] += 1




    pprint.pprint(towns)
    pprint.pprint(zip_codes)
    #pprint.pprint(streets)
    #pprint.pprint(keys)
    #pprint.pprint(bad_coords)

filename = "../ex_JJ1igoeA8K3YfUHPuiifFYRg8LHik.osm"
#filename = "../pittsburgh.osm"

count_stuff(filename)
