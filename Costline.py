from osgeo import gdal
from osgeo import ogr

# Åpne geotiff-filen
ds = gdal.Open('input_file.tiff')

# Opprett et OGR-lag
ogr_ds = ogr.Open(ds)
layer = ogr_ds.GetLayer()

# Opprett en linje-geometri for kystlinjen
line = ogr.Geometry(ogr.wkbLineString)

# Gå gjennom hvert punkt i kystlinjen og legg til i linje-geometrien
for feature in layer:
    geometry = feature.GetGeometryRef()
    line.AddPoint(geometry.GetX(), geometry.GetY())

# Lag en ny fil for å lagre resultatet
out_ds = ogr.GetDriverByName('ESRI Shapefile').CreateDataSource('output_file.shp')
out_layer = out_ds.CreateLayer('kystlinje', geom_type=ogr.wkbLineString)

# Opprett et OGR-feature og legg til linje-geometrien
out_feature = ogr.Feature(out_layer.GetLayerDefn())
out_feature.SetGeometry(line)

# Legg til featuret i laget
out_layer.CreateFeature(out_feature)

# Lagre endringer og lukk filene
out_ds.Destroy()
ogr_ds.Destroy()
