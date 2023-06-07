class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
#print(issubclass(TrackedVehicle,(Vehicle,LandVehicle)))
#for cls1 in [Vehicle,LandVehicle,TrackedVehicle]:
    #for cls2 in [Vehicle,LandVehicle,TrackedVehicle]:
        #print(issubclass(cls1, cls2), end="\t")
        #print()

v=Vehicle()
lv=LandVehicle()
tv=TrackedVehicle()

for cls1 in [v,lv,tv]:
    for cls2 in [Vehicle,LandVehicle,TrackedVehicle]:
        print(isinstance (cls1, cls2), end="\t")
    print()

