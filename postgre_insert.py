import gpxpy;
import gpxpy.gpx;
import psycopg2;

with open("test_files_gpxpy/test_files/cerknicko-jezero.gpx", "r") as gpx_test:
    gpx_file = gpxpy.parse(gpx_test)
    print(gpx_file)
    