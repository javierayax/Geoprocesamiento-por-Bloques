#grid = arcpy.GridIndexFeatures_cartography("in_memory\grid", "Predios_Nacionales", "INTERSECTFEATURE", polygon_width = "20 kilometers", polygon_height = "20 kilometers")
#arcpy.DeleteRows_management("Predios_test")
import time, arcpy, multiprocessing, Queue

def intersectar(poly):
    t1 = time.clock()
    arcpy.SelectLayerByLocation_management(predios, "HAVE_THEIR_CENTER_IN", poly)
    p = r"in_memory/predioTemp"
    arcpy.Intersect_analysis("%s #;%s #" % (predios.name, cancha.name), out_feature_class = p)
    arcpy.Append_management(p, PrediosTotal, "NO_TEST")
    arcpy.AddMessage(str(time.clock()-t1))


TIMEOUT = 10
PrediosTotal = "Predios_test"
t0 = time.clock()

predios = arcpy.GetParameter(0)
cancha = arcpy.GetParameter(1)
grilla = arcpy.GetParameter(2)

polys = arcpy.CopyFeatures_management(grilla, arcpy.Geometry())
for poly in polys:
    intersectar(poly)

arcpy.AddMessage(time.clock()-t0)
arcpy.SetParameter(3, PrediosTotal)