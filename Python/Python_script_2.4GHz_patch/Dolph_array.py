from ansys.aedt.core import Hfss

hfss = Hfss(
    project="Antenna_array",
    design="Dolph_array",
    version="2024.2",
    new_desktop=False,
)
hfss["Inset_depth"] = "14.9917mm"

#Good result till now
#5.36GHz BW 150MHz
'''width = 44
length = 29.42
cut = 4
gnd = 100
sub_thick = 1.6
lambada = 58.8023789699
rect_width = 0.1*lambada
rect_length = lambada/2'''

'''[width = 52
length = 29.42
extra = 29.42-length
cut = 4
gnd = 100
sub_thick = 1.6
lambada = 58.8023789699
rect_width = 0.1*lambada
rect_length = lambada/2'''


#length = 58.4
#length = 62.4
width = 27.9
length = 62.4
cut = 4
gnd = 100
sub_length = 76.8
sub_width = 57.8
sub_thick = 1.6
extra = sub_width-width
feed_length = 14.45
feed_2_length = 9.25
feed_width = 3.1
lambada = 58.8023789699
rect_width = 0.1*lambada
rect_length = lambada/2



x = hfss.modeler

substrate = x.create_box(origin=[-sub_length/2,-sub_width/2,0],
                         sizes=[76.8,57.8,sub_thick],
                         name="subsstrate",
                         material="FR4_epoxy")

ground_plane = x.create_rectangle(orientation="XY",
                           origin=[-sub_length/2,-sub_width/2,0],
                           sizes=[sub_length,50],
                           material="copper",
                           name="Ground_Plane")

'''rect_2 = x.create_rectangle(orientation="XY",
                            origin=[-rect_length/2,-rect_width/2+8,0],
                            sizes=[rect_length,rect_width],
                            name="slot")
x.subtract("Ground_Plane","slot")'''


patch = x.create_rectangle(orientation="XY",
                           origin=[-length/2,-width/2,sub_thick],
                           sizes=[length,width],
                           material="copper",
                           name="Patch_antenna")


feed = x.create_rectangle(orientation="XY",
                          origin=[-((feed_width/2)),-sub_width/2,sub_thick],
                          sizes=[feed_width,extra],
                          material="copper",
                          name = "Feed")

hfss.assign_finite_conductivity("Patch_antenna",
                                material="copper",
                                name="Patch_antenna")

hfss.assign_finite_conductivity("Ground_Plane",
                                material="copper",
                                name="Ground")
x.create_rectangle(orientation="XZ",
                   origin=[-feed_width/2,-sub_width/2,0],
                   sizes=[sub_thick,feed_width],
                   name="Lumped_port")

hfss.lumped_port(assignment="Lumped_port",
                 reference="Ground_Plane",
                 integration_line=[[0,-sub_width/2,0],
                                   [0,-sub_width/2,sub_thick]],
                 impedance=50,
                 name="Lumped_port")






'''opti = hfss.optimizations.add(calculation="dB(S(1,1))",
                              ranges={"Freq": "2.4GHz"},
                              optimization_type="Optimization")

opti.add_variation(variable_name="Inset_depth",
                   min_value=0.01,
                   max_value=19)
opti.add_goal(calculation="dB(S(1,1))",
              ranges={"Freq": "2.4GHz"},
              condition="Minimize")

opti.analyze(cores = 4, tasks=4)'''


rect = x.create_rectangle(orientation="XY",
                          origin=[-cut,-width/2,sub_thick],
                          sizes=[cut*2,"Inset_depth"],
                          name = "rect")

x.subtract("Patch_antenna","rect")


feed_2 = x.create_rectangle(orientation="XY",
                            origin=[-((feed_width/2)+1),-width/2,sub_thick],
                            sizes=[((feed_width/2)+1)*2,"Inset_depth"],
                            name = "feed_2")
x.unite("Feed,feed_2")
x.unite("Patch_antenna,Feed")

hfss.create_open_region(frequency="2.4GHz",
                        boundary="Radiation")


setup = hfss.create_setup(name="Setup_1"
                  )

sweep = hfss.create_linear_count_sweep(setup="Setup_1",
                                       units="GHz",
                                       start_frequency=1,
                                       stop_frequency=10,
                                       num_of_freq_points=300)

hfss.analyze_setup(name="Setup_1", cores=4,tasks=4)

















