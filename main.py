from flask import Flask
from flask import request,Response
import csv
import json
import bisect
from math import sqrt as SQRT
from math import asin as ASIN
from math import sin as SIN
from math import cos as COS
from math import pi as PI

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
coords = [None]*100
sorted_areas = []
sorted_coordinates = []
with open("numeric_cc.csv") as csvfile:
    locations = csv.reader(csvfile)
    locations.next()
    counter  = 0
    for _,area,lat,lon in locations:
        area = area.lower()
        counter = counter + 1
        sorted_areas.append(area)
        sorted_coordinates.append((lat, lon))
        ilat = int(float(lat))
        ilon = int(float(lon))
        if coords[ilat] is None:
            coords[ilat] = [[] for _ in xrange(100)]
        coords[ilat][ilon].append((area,lat,lon))

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/area_coordinates')
def get_area_coordinates():
    """Return a friendly HTTP greeting."""
    area = request.args.get('area')
    area = area.lower()
    lat,lon = get_coordinates(sorted_areas, sorted_coordinates, area)
    if lat is None:
        return Response(json.dumps([]), mimetype='application/json')
    return Response(json.dumps([lat,lon]), mimetype='application/json')

@app.route('/nearby_areas/blocks')
def nearby_areas_blocks():
    """Return a friendly HTTP greeting."""
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    area = request.args.get('area')
    if area and not(lat and lon):
        area = area.lower()
        lat,lon = get_coordinates(sorted_areas, sorted_coordinates, area)
    if lat and lon:
        flat = float(lat)
        flon = float(lon)
        blocks = get_nearby(coords, flat, flon)
        return Response(json.dumps(blocks), mimetype='application/json')
    return Response(json.dumps([]), mimetype='application/json')


@app.route('/nearby_areas/sorted')
def nearby_areas_sorted():
    """Return a friendly HTTP greeting."""
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    area = request.args.get('area')
    if area and not(lat and lon):
        area = area.lower()
        lat,lon = get_coordinates(sorted_areas, sorted_coordinates, area)
    if lat and lon:
        flat = float(lat)
        flon = float(lon)
        blocks = get_nearby(coords, flat, flon)
        allareas = reduce(lambda x,y: x+y, blocks)
        print allareas
        allareas = gc_append_sd(allareas, flat, flon,i=1,j=2)
        allareas = sorted(allareas, key=lambda e:e[3])
        return Response(json.dumps(allareas), mimetype='application/json')
    return Response(json.dumps([]), mimetype='application/json')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


def get_nearby(a, lat,lon):
    ilat = int(lat)
    ilon = int(lon)
    dirs =[(-1,-1),(1,1),(1,0),(0,-1),(-1,0),(0,1),(-1,1),(1,-1),(0,0)]
    #return [a[ilat + d[0]][ilon + d[1]] for d in dirs if a[ilat - d[0]] is not None]
    result = []
    for d in dirs:
        #print ilat - d[0]
        if a[ilat - d[0]] is None:
            result.append([])
        else:
            result.append(a[ilat + d[0]][ilon + d[1]])
    return result


def get_coordinates(sa, sc, area):
    li = bisect.bisect_left(sa, area)
    if sa[li] == area:
        return sc[li]
    return [None,None]


def get_nearby_areas(coords, sa, sc, area):
    lat,lon = get_coordinates(sa, sc, area)
    return(get_nearby(coords, lat, lon))

def gc_append_sd(sl, lat, lng,i=3,j=4):
    #sd_list = [(2*ASIN(SQRT((SIN((lat*(PI/180)-e[i]*(PI/180))/2))**2+COS(lat*(PI/180))*COS(e[i]*(PI/180))*(SIN((lng*(PI/180)-e[j]*(PI/180))/2))**2)))*(180*60/PI*1852)/1000 for e in sl]
    try:
        sdl = [list(e) + [((2*ASIN(SQRT((SIN((lat*(PI/180)-float(e[i])*(PI/180))/2))**2+COS(lat*(PI/180))*COS(float(e[i])*(PI/180))*(SIN((lng*(PI/180)-float(e[j])*(PI/180))/2))**2)))*(180*60/PI*1852)/1000)*1.3142135] for e in sl]
    except ValueError:
        sdl = ["ValueError"]
    return sdl
