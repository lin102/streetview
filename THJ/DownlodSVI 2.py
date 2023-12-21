import csv
import streetview
import numpy as np

input_path = '/Volumes/THJ/streetview/'

with open(input_path + 'SVI_points_JTH_2.csv', 'r', encoding='utf-8')as f:
    data = list(csv.reader(f))
    SVI_none = []
    for row in data:
        lat = row[1]
        lon = row[2]
        panoids = streetview.panoids(lat, lon)
        temp_dir = input_path + 'Temp'
        outfile = input_path + 'GSV11/'
        if len(panoids) == 0:
            SVI_none = np.append(SVI_none, [lat, lon], axis=0)
            continue


        years = [item['year'] for item in panoids for key in item if key == 'year']
        print(years)

        if len(years) == 0:
            panoid = panoids[0]['panoid']
            tiles = streetview.tiles_info(panoid)
            streetview.download_tiles(tiles, temp_dir, disp=False)
            streetview.stich_tiles(panoid, tiles, temp_dir, outfile, lon, lat, 0, 0)
            streetview.delete_tiles(tiles, temp_dir)
            continue

        latest_year = max(years)

        for gsvid in panoids:
            if 'year' in gsvid.keys() and gsvid['year'] == latest_year:
                if 'month' in gsvid.keys():
                    month = gsvid['month']
                else:
                    month = 0
                panoid = gsvid['panoid']
                tiles = streetview.tiles_info(panoid)
                streetview.download_tiles(tiles, temp_dir, disp=False)
                streetview.stich_tiles(panoid, tiles, temp_dir, outfile, lon, lat, latest_year, month)
                streetview.delete_tiles(tiles, temp_dir)
                break



    np.savetxt(input_path + "none_points.csv", SVI_none, delimiter=",")


