import numpy as np
from siman.calc_manage import smart_structure_read
from siman.geo import hkl2uvw, three2four_index, create_supercell, four2three_index

# perpendicular_vector = np.cross([1,-1,4], [-1,-1,0])
# temp = three2four_index(perpendicular_vector)
# print(temp)
# temp = four2three_index(temp)
# print(temp)

# perpendicular_vector = np.cross([1,-1,2], [-1,-1,0])
# temp = three2four_index(perpendicular_vector)
# print(temp)
# temp = four2three_index(temp)
# print(temp)
# temp = four2three_index(three2four_index())


def grain_const(input_str_path='', gb_plane=[], rot_axis=[], mul=(1, 1, 1)):
    """
    Construct grain by finding directions from GB plane and rotation axis

    INPUT:
            - input_str_path - string, path to your initial structure
            - angle - integer, angle of disorientation between two grains, deafault 60 degree, the primitive cell will be rotated to angle/2
            - angle_axis - list, axis along which the rotation will be performed, 3 Miller indices, deafault [0,0,1]
            - gb_plane - list, plane in which the GB will be created, 3 Miller indices
            - rot_axis - list, axis using which the GB will be constructed, 3 Miller indices
            - mul - tuple, multiplication matrix used for decreasing the grain cell size, deafault (1,1,1)

    OUTPUT:
            - sc (siman.structure) - cell of the grain for the further GB construction

    """

    st = smart_structure_read(input_geo_file=input_str_path)
    # print(st1.rprimd)
    # print(st.rprimd)
    # print(angle/2)
    # uvt = hkl2uvw(gb_plane, st1.rprimd)
    uvtw1 = three2four_index(hkl2uvw(gb_plane, st.rprimd))  # rprimd problem
    # uvt1 = four2three_index(uvtw1)
    uvt1 = four2three_index(uvtw1)
    # print(hkl2uvw(gb_plane, st1.rprimd) )
    # uvt1 = list(-np.array(uvt1))
    # print(rot_axis)
    # rot_axis = list(-np.array(rot_axis))

    # print(uvtw1)
    # print(uvt1)
    # print(rot_axis)
    uvt2 = np.cross(uvt1, rot_axis)
    # print(uvt2)
    # uvt2 = np.cross(gb_plane,  uvt1)
    # uvt2 = np.cross(gb_plane,  rot_axis)
    # print('1',uvt2)
    # print('2',three2four_index(np.cross(gb_plane,  rot_axis)))
    # print('3', four2three_index(three2four_index(np.cross(gb_plane,  rot_axis))))
    uvt2 = four2three_index(three2four_index(np.cross(rot_axis, gb_plane)))
    # print(uvt2)
    # uvt2 = [-1,1,1]
    # print(uvt2)
    # uvt2 = list(-np.array(uvt2))
    # print(uvt2)
    # print(rot_axis)
    # vol = np.dot(uvt2, np.cross(uvt1, rot_axis))
    # print(vol)§
    print('GB plane', gb_plane)
    print('First vector (perpendicular to the GB plane):', uvt1)
    print('Second vector:', uvt2)
    print('Third vector (rotaion axis):', rot_axis)
    # mul = mul
    # print(mul)
    sc = create_supercell(st, [uvt1, uvt2, rot_axis], mul=mul)

    return sc


# TESTS

# vol = np.dot([   4.34,   -2.51, -229.94], np.cross([ 34.71,   -20.04,  14.37], [   1.45,    2.51,    0.  ]))
# vol = np.dot([8, -8, 1], np.cross([-1, 1, 16], [-1, -1, 0]))
# print(vol)
gr = grain_const(
    '/Users/ndavydov/Documents/Skoltech/Science/cifs/POSCAR_LiNiO2_r3m_su_4uiAg_100_end_from_dima_aks', [-1, 1, -2], [-1, -1, 0])
# gr.write_poscar('POSCAR_grain_s_5')
# gr = grain_const('/Users/ndavydov/Documents/Skoltech/Science/cifs/POSCAR_LiNiO2_r3m_su_4uiAg_100_end_from_dima_aks', [1,-1,-4], [-1,-1,0] )
# gr.write_poscar('POSCAR_grain_s_2')

# hkl1 1 -1 -4  #twin plane: should be parrallel to uvtw2 and uvtw3

# uvtw1  4 -4 0  -1 #direction close to normal to hkl1 twin plane
# uvtw2  2 -2 0   1 # Usually sliding direction, but should be perpendicular to uvtw3 and parallel to hkl1
# uvtw3 -1 -1 2  0

# print(gr)
# st = smart_structure_read(input_geo_file = '/Users/ndavydov/Documents/Skoltech/Science/cifs/POSCAR_LiNiO2_r3m_su_4uiAg_100_end_from_dima_aks')
# print(st1.check_JT())
# print(st1.rprimd)
# print(dir(st1))
# lat = st1.rprimd()
# mul = (1,1,1)
# print (type(mul))
# st1 = st.rotate([0,0,1], 60/2)

# sc = create_supercell(st1, [[4, -4, -1],[2, -2, 1],[-1, -1, 0]], mul = (1,1,1))
# sc.write_poscar('POSCAR_s2_2')
