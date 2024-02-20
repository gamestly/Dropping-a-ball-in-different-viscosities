G = 6.6743 * pow(10,-11)
mass_earth = 5.972*pow(10,24)
radius_earth = 6.378 * pow(10,6)
def gravitaion_force(mass1 , mass2 , distance):
    F_G = G*mass1*mass2/(distance**2)
    return F_G

print(gravitaion_force(1.9885*pow(10,30),5.972*pow(10,24),1.496*pow(10,11)))

def g_surface():
    g_earth = G*mass_earth/pow(radius_earth,2)
    return g_earth

print(g_surface())