
import os
import numpy as np

def create_base_directory(geometry):
    root = os.getcwd()
    geometry_dir = os.path.join(root, geometry)
    if not os.path.isdir(geometry_dir):
        os.mkdir(geometry_dir)
        return geometry_dir
    else:
        return geometry_dir

def create_holes_directories(base, N_roles, R_holes):
    N_roles_dir_name = '{}_holes_R{}'.format(N_roles, int(R_holes*1000))
    N_roles_subdir = os.path.join(base, N_roles_dir_name)
    if not os.path.isdir(N_roles_subdir):
        os.mkdir(N_roles_subdir)
    return N_roles_subdir  

def create_temperature_subdirectory(N_roles_subdir, T):
    T_subdirs = []    
    T_subdir = os.path.join(N_roles_subdir, 'T{}'.format(T))
    if not os.path.isdir(T_subdir):
        os.mkdir(T_subdir)
    T_subdirs.append(T_subdir)
    return T_subdirs

def create_temperature_subdirectories(T_subdirs):
    energylog_dirs = []
    hysteresis_dirs = []    
    groundstates_dirs = []
    scripts_dirs = []
    plots_dirs = []
    # subdirs
    sub_dirs = ['cubit',
                'energylog',
                'final_path',
                'groundstates',
                'hysteresis',
                'initial_path',
                'NEB',
                'patran',
                'plots',
                'scripts']
    # for each elongation, creates the subdirs
    for T_subdir in T_subdirs:
        for sub_dir in sub_dirs:
            new_sub_dir = os.path.join(T_subdir,sub_dir)
            if not os.path.isdir(new_sub_dir):
                os.mkdir(new_sub_dir)
            # energgylog
            if sub_dir == 'energylog':
                energylog_dirs.append(new_sub_dir)
            # hysteresis
            elif sub_dir == 'hysteresis':
                hysteresis_dirs.append(new_sub_dir)
            # scripts
            elif sub_dir == 'scripts':
                scripts_dirs.append(new_sub_dir)
            # groundstates
            elif sub_dir == 'groundstates':
                groundstates_dirs.append(new_sub_dir)
            # plots
            elif sub_dir == 'plots':
                plots_dirs.append(new_sub_dir)
    return [energylog_dirs, 
            hysteresis_dirs, 
            groundstates_dirs,
            scripts_dirs,
            plots_dirs]
            
def create_energylog_subdirs(energylog_dirs, sizes):
    subdirs, groundstates_subdirs = [], []
    energylog_sub_dirs = ['groundstates','energy_barriers']
    for energylog_dir in energylog_dirs:
        for energylog_sub_dir in energylog_sub_dirs:
            path = os.path.join(energylog_dir, energylog_sub_dir)
            if not os.path.isdir(path):
                os.mkdir(path)
            if energylog_sub_dir == 'groundstates':
                for size in sizes:
                    size_path = os.path.join(path, str(size))
                    if not os.path.isdir(size_path):
                        os.mkdir(size_path)
                    groundstates_subdirs.append(size_path)
            subdirs.append(path)
    
def create_hysteresis_subdirs(hysteresis_dirs, sizes):
    groundstates_subdirs, loops_subdirs, size_hyst_subdirs = [], [], []
    hysteresis_sub_dirs = ['groundstates','loops', 'size_loop']
    for hysteresis_dir in hysteresis_dirs:
        for hysteresis_sub_dir in hysteresis_sub_dirs:
            path = os.path.join(hysteresis_dir, hysteresis_sub_dir)
            if not os.path.isdir(path):
                os.mkdir(path)
            if hysteresis_sub_dir == 'groundstates':
                for size in sizes:
                    size_path = os.path.join(path, str(size))
                    if not os.path.isdir(size_path):
                        os.mkdir(size_path)
                    groundstates_subdirs.append(size_path)
            if hysteresis_sub_dir == 'loops':
                for size in sizes:
                    loops_subdir = os.path.join(path, str(size))
                    if not os.path.isdir(loops_subdir):
                        os.mkdir(loops_subdir)
                    loops_subdirs.append(loops_subdir)
            if hysteresis_sub_dir == 'size_loop':
                for sub in ['states','hyst']:
                    sub_path = os.path.join(path, sub)
                    if not os.path.isdir(sub_path):
                        os.mkdir(sub_path)
                    size_hyst_subdirs.append(size_path)
            else:
                loops_subdirs.append(path)         
                
def create_scripts_subdirs(scripts_dirs, sizes):
    scripts_sub_dirs = ['groundstates','energy_barrier', 'batch', 'hysteresis', 'size_hysteresis']
    for scripts_dir in scripts_dirs:
        for scripts_sub_dir in scripts_sub_dirs:
            path = os.path.join(scripts_dir, scripts_sub_dir)
            if not os.path.isdir(path):
                os.mkdir(path)
            if scripts_sub_dir == 'hysteresis':
                for size in sizes:
                    ss = os.path.join(path, str(size))
                    if not os.path.isdir(ss):
                        os.mkdir(ss)
        
def create_groundstates_subdirs(groundstates_dirs, sizes): 
    for groundstates_dir in groundstates_dirs:
        for size in sizes:
            path = os.path.join(groundstates_dir, str(size))
            if not os.path.isdir(path):
                os.mkdir(path)           
                        
def create_all_directories(geometry, N_roles, Ts, sizes, R_holes):
    base = create_base_directory(geometry)
    for N_role in N_roles:
        for T in Ts:
            hole_dir = create_holes_directories(base, N_role, R_holes)
            temp_dir = create_temperature_subdirectory(hole_dir, T)
            temp_subdirs = create_temperature_subdirectories(temp_dir)
            # sub directories
            energylog_dirs = temp_subdirs[0]
            hysteresis_dirs = temp_subdirs[1]
            groundstates_dirs = temp_subdirs[2]
            scripts_dirs = temp_subdirs[3]
            plots_dirs = temp_subdirs[4]
            # sub sub directories
            create_energylog_subdirs(energylog_dirs, sizes)
            create_hysteresis_subdirs(hysteresis_dirs, sizes)
            create_scripts_subdirs(scripts_dirs, sizes)
            create_groundstates_subdirs(groundstates_dirs, sizes)

def get_random_position(N_holes): 
    positions = []
    for i in range(N_holes):
        r = 2 * (np.random.rand(3) - 0.5)
        while (r[0]**2 + r[1]**2 + r[2]**2) > 1:
            r = 2 * (np.random.rand(3) - 0.5)
        positions.append(r)
    return np.array(positions) 

def hole_position(p, size, R_holes): 
    return p * (size/2 - R_holes) 

def create_swiss_cheese_mesh(geometry, N_holes, Ts, size, R_holes, p):
    meshsize = 0.009
    s = '#!python \n'
    s += 'import cubit \n'
    s += 'cubit.init([""]) \n'
    s += "cubit.cmd(\"brick x {0:g}\") \n".format(size/1000)
    n_swiss_cheese = 1
    n_hole = 2
    for n in range(len(p)):
        s += "cubit.cmd(\"create sphere radius {0:g}\") \n".format(R_holes)
        r = p[n]
        s += "cubit.cmd(\"volume {0:g} move x {1:g} y {2:g} z {3:g} \")  \n".format(n_hole, r[0]/1000, r[1]/1000, r[2]/1000)
        s += "cubit.cmd(\"subtract volume {0:g} from volume {1:g}\") \n".format(n_hole, n_swiss_cheese)
        n_swiss_cheese = n_hole + 1
        n_hole = n_swiss_cheese + 1
    s += "cubit.cmd(\"volume {0:g} size {1:g}\")\n".format(n_swiss_cheese, meshsize)
    s += "cubit.cmd(\"volume {0:g} scheme Tetmesh\") \n".format(n_swiss_cheese)
    s += "cubit.cmd(\"mesh volume {0:g}\") \n".format(n_swiss_cheese)
    s += "cubit.cmd(\"block 1 volume {0:g}\") \n".format(n_swiss_cheese)
    s += "cubit.cmd(\"block 1 element type tetra4\") \n"
    base = create_holes_directories(create_base_directory(geometry), N_holes, R_holes)
    for i in range(len(Ts)):
        if i == 0:
            cubit_file_path = os.path.join(base,
                                          'T{}'.format(Ts[i]),
                                          'cubit',
                                          's{0:g}_N{1:g}_T{2:g}_R{3:g}.jou'.format(size, N_holes, Ts[i], R_holes*1000))
            patran_file_path = os.path.join(base,
                                            'T{}'.format(Ts[i]),
                                            'patran',
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}.pat'.format(size, N_holes, Ts[i], R_holes*1000))
            full_path = "/" + "/".join(patran_file_path.split('\\')[1:])
            s += 'cubit.cmd(\"export patran \'C:{}\' overwrite\") \n'.format(full_path)
            s += "cubit.cmd(\"reset\") \n"
            with open(cubit_file_path, 'w') as f:
                f.write(s)
        else:
            cubit_file_path_previous = os.path.join(base,
                                                    'T{}'.format(Ts[i-1]),
                                                    'cubit',
                                                    's{0:g}_N{1:g}_T{2:g}_R{3:g}.jou'.format(size, N_holes, Ts[i-1], R_holes*1000))
            with open(cubit_file_path_previous, 'r') as f:
                content = f.readlines()
            for j in range(len(content[:-1])):
                if j == 0:
                    s = content[j]
                else:
                    s += content[j]                          
            cubit_file_path_new = os.path.join(base,
                                              'T{}'.format(Ts[i]),
                                              'cubit',
                                              's{0:g}_N{1:g}_T{2:g}_R{3:g}.jou'.format(size, N_holes, Ts[i], R_holes*1000))
            patran_file_path = os.path.join(base,
                                            'T{}'.format(Ts[i]),
                                            'patran',
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}.pat'.format(size, N_holes, Ts[i], R_holes*1000))
            full_path = "/" + "/".join(patran_file_path.split('\\')[1:])
            s += 'cubit.cmd(\"export patran \'C:{}\' overwrite \") \n'.format(full_path)
            s += "cubit.cmd(\"reset\") \n"
            with open(cubit_file_path_new, 'w') as f:
                f.write(s)
                
def create_swiss_cheese_meshes(geometry, N_holes, Ts, sizes, R_holes):
    for N_hole in N_holes:
        p = get_random_position(N_hole)
        for size in sizes:
            r = hole_position(p, size, R_holes)
            create_swiss_cheese_mesh(geometry, N_hole, Ts, size, R_holes, r)

def create_cubit_python_script(geometry, N_holes, Ts, R_holes):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            cubit_dir_path = os.path.join(base,
                                         '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                                         'T{}'.format(T),
                                         'cubit')
            python_script_path = os.path.join(cubit_dir_path, 'N{0:g}_T{1:g}_R{2:g}_meshes.py'.format(N_hole, T, R_holes*1000))
            with open(python_script_path, 'w') as f:
                f.write('#!python \n')
                f.write('import cubit \n')
                f.write('cubit.init([""]) \n')
                f.write('cubit.cmd(\"set journal off\") \n')
                for cubit_script in os.listdir(cubit_dir_path):
                    if 'meshes' not in os.path.splitext(cubit_script)[0]:
                        cubit_script_path = os.path.join(cubit_dir_path, cubit_script)
                        with open(cubit_script_path, 'r') as cubitf:
                            content = cubitf.readlines()
                        for line in content[3:]:
                            f.write('{}'.format(line))
                        f.write("\n")      
                
def execute_cubit_python_script(geometry, N_holes, Ts, R_holes):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            path = os.path.join(base,
                               '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                               'T{}'.format(T),
                               'cubit',
                               'N{0:g}_T{1:g}_R{2:g}_meshes.py'.format(N_hole, T, R_holes*1000))
            # execute
            print(path)
            os.system('cubit_python {}'.format(path))

def create_swiss_cheese_groundstates_script(geometry, N_holes, Ts, sizes, R_holes, n_lem):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            gs_dir_path = os.path.join(base,
                                         '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                                         'T{}'.format(T),
                                         'scripts',
                                         'groundstates')
            patran_dir_path = os.path.join(base,
                                         '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                                         'T{}'.format(T),
                                         'patran')
            for size in sizes:
                filename = 's{0:g}_N{1:g}_T{2:g}_R{3:g}'.format(size, N_hole, T, R_holes*1000)      
                patran_filepath = os.path.join(patran_dir_path, filename + '.pat')
                patran_filepath = "/" + "/".join(patran_filepath.split('\\')[1:])
                with open(os.path.join(gs_dir_path, filename), 'w') as f:
                    f.write("Magnetite {} C \n".format(T))
                    f.write("ReadMesh 1 {} \n".format(patran_filepath))
                    for i in range(1, n_lem + 1):
                        f.write("! Random state # {} \n ".format(i))
                        f.write("Randomize All Moments \n")
                        energylog_path = os.path.join(base,
                                         '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                                         'T{}'.format(T),
                                         'energylog',
                                         'groundstates',
                                         str(size),
                                         filename + '_{}'.format(i))
                        energylog_path = "/" + "/".join(energylog_path.split('\\')[1:])
                        f.write("Energylog {} \n".format(energylog_path))
                        f.write("Minimize \n")
                        gs_path = os.path.join(base,
                                              '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                                              'T{}'.format(T),
                                              'groundstates',
                                              str(size),
                                              filename + '_{}'.format(i))
                        gs_path = "/" + "/".join(gs_path.split('\\')[1:])
                        f.write("WriteMagnetization {} \n".format(gs_path))
                        hyst_path = os.path.join(base,
                                              '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                                              'T{}'.format(T),
                                              'hysteresis',
                                              'groundstates',
                                              str(size),
                                              filename + '_{}'.format(i))
                        hyst_path = "/" + "/".join(hyst_path.split('\\')[1:])
                        f.write("WriteHyst {} \n".format(hyst_path))
                        f.write("CloseLogFile \n")
                        f.write("\n")

def create_batch_script_groundstates(geometry, N_holes, Ts, sizes, R_holes):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            mscripts_dir = os.path.join(base,
                                         '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                                         'T{}'.format(T),
                                         'scripts',
                                         'groundstates')
            batch_script_path = os.path.join(base,
                                         '{}_holes_R{}'.format(N_hole, int(R_holes*1000)),
                                         'T{}'.format(T),
                                         'scripts',
                                         'batch',
                                         'N{0:g}_T{1:g}_R{2:g}_groundstates.bat'.format(N_hole, T, R_holes*1000))
            with open(batch_script_path, 'w') as f:
                for file in os.listdir(mscripts_dir):
                    filepath = os.path.join(mscripts_dir, file)
                    f.write('merrill {} \n'.format(filepath))
                    
def create_hysteresis_scripts(geometry, N_holes, Ts, sizes, R_holes, H):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            for size in sizes:
                patran_path = os.path.join(base,
                                          '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                          'T{0:g}'.format(T),
                                          'patran',
                                          's{0:g}_N{1:g}_T{2:g}_R{3:g}.pat'.format(size, N_hole, T, R_holes*1000))
                patran_path = "/" + "/".join(patran_path.split('\\')[1:])
                Hx, Hy, Hz = H                                                                      
                hyst_script_path = os.path.join(base,
                                                '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                                'T{0:g}'.format(T),
                                                'scripts',
                                                'hysteresis',
                                                str(size),
                                                's{0:g}_N{1:g}_T{2:g}_R{3:g}_{4:g}_{5:g}_{6:g}'.format(size,
                                                                                                      N_hole,
                                                                                                      T,
                                                                                                      R_holes*1000,
                                                                                                      round(Hx[0],2),
                                                                                                      round(Hy[0],2),
                                                                                                      round(Hz[0],2)))
                with open(hyst_script_path, 'w') as f:                    
                    f.write("! Hysteresis loops")
                    f.write(" \n")
                    f.write("Set MaxMeshNumber 1 \n")
                    f.write("Set MaxEnergyEvaluations 10000 \n")
                    f.write("Magnetite {0:g} C \n".format(T))
                    f.write("ReadMesh 1 {} \n".format(patran_path))           
                    f.write("External Field Direction {} {} {} \n".format(Hx[0], Hy[0], Hz[0]))
                    f.write("External Field Strength 0 mT \n")
                    f.write("Uniform Magnetization 1 1 1  \n")
                    # loop 1
                    f.write("Loop field 500 100 -20 \n")
                    f.write("   Randomize Magnetization 10 \n")
                    f.write("   External Field Strength #field mT \n")
                    f.write("   Minimize \n")   
                    hyst_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'hysteresis',
                                            'loops',
                                            str(size),
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_{4:g}_{5:g}_{6:g}'.format(size,
                                                                                                      N_hole,
                                                                                                      T,
                                                                                                      R_holes*1000,
                                                                                                      round(Hx[0],2),
                                                                                                      round(Hy[0],2),
                                                                                                      round(Hz[0],2)))
                    hyst_path = "/" + "/".join(hyst_path.split('\\')[1:])
                    f.write("   WriteHyst {} \n".format(hyst_path))
                    gs_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'hysteresis',
                                            'loops',
                                            str(size),
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_{4:g}_{5:g}_{6:g}_#field_mT'.format(size,
                                                                                                      N_hole,
                                                                                                      T,
                                                                                                      R_holes*1000,
                                                                                                      round(Hx[0],2),
                                                                                                      round(Hy[0],2),
                                                                                                      round(Hz[0],2)))
                    gs_path = "/" + "/".join(gs_path.split('\\')[1:])
                    f.write("   WriteMagnetization {} \n".format(gs_path))
                    f.write("EndLoop \n")
                    # loop 2
                    f.write("Loop field 100 -100 -5 \n")
                    f.write("   Randomize Magnetization 10 \n")
                    f.write("   External Field Strength #field mT \n")
                    f.write("   Minimize \n")
                    hyst_path = os.path.join(base,
                                                '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                                'T{0:g}'.format(T),
                                                'hysteresis',
                                                'loops',
                                                str(size),
                                                's{0:g}_N{1:g}_T{2:g}_R{3:g}_{4:g}_{5:g}_{6:g}'.format(size,
                                                                                                      N_hole,
                                                                                                      T,
                                                                                                      R_holes*1000,
                                                                                                      round(Hx[0],2),
                                                                                                      round(Hy[0],2),
                                                                                                      round(Hz[0],2)))
                    hyst_path = "/" + "/".join(hyst_path.split('\\')[1:])
                    f.write("   WriteHyst {} \n".format(hyst_path))
                    gs_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'hysteresis',
                                            'loops',
                                            str(size),
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_{4:g}_{5:g}_{6:g}_#field_mT'.format(size,
                                                                                                      N_hole,
                                                                                                      T,
                                                                                                      R_holes*1000,
                                                                                                      round(Hx[0],2),
                                                                                                      round(Hy[0],2),
                                                                                                      round(Hz[0],2)))
                    gs_path = "/" + "/".join(gs_path.split('\\')[1:])
                    f.write("   WriteMagnetization {} \n".format(gs_path))
                    f.write("EndLoop \n")
                    # loop 3
                    f.write("Loop field -100 -500 -20 \n")
                    f.write("   Randomize Magnetization 10 \n")
                    f.write("   External Field Strength #field mT \n")
                    f.write("   Minimize \n")  
                    hyst_path = os.path.join(base,
                                                '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                                'T{0:g}'.format(T),
                                                'hysteresis',
                                                'loops',
                                                str(size),
                                                's{0:g}_N{1:g}_T{2:g}_R{3:g}_{4:g}_{5:g}_{6:g}'.format(size,
                                                                                                      N_hole,
                                                                                                      T,
                                                                                                      R_holes*1000,
                                                                                                      round(Hx[0],2),
                                                                                                      round(Hy[0],2),
                                                                                                      round(Hz[0],2)))
                    hyst_path = "/" + "/".join(hyst_path.split('\\')[1:])
                    f.write("   WriteHyst {} \n".format(hyst_path))
                    gs_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'hysteresis',
                                            'loops',
                                            str(size),
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_{4:g}_{5:g}_{6:g}_#field_mT'.format(size,
                                                                                                      N_hole,
                                                                                                      T,
                                                                                                      R_holes*1000,
                                                                                                      round(Hx[0],2),
                                                                                                      round(Hy[0],2),
                                                                                                      round(Hz[0],2)))
                    gs_path = "/" + "/".join(gs_path.split('\\')[1:])
                    f.write("   WriteMagnetization {}  \n".format(gs_path))
                    f.write("EndLoop \n")  
                    
def field_components(theta, phi):
    hx = np.sin(theta)*np.sin(phi)
    hy = np.cos(theta)
    hz = np.sin(theta)*np.cos(phi)
    if hx < 1e-10:
        hx = 0
    if hy < 1e-10:
        hy = 0
    if hz < 1e-10:
        hz = 0
    return hx, hy, hz

def create_batch_script_hysteresis(geometry, N_holes, Ts, sizes, R_holes):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            batch_script_path = os.path.join(base,
                                                '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                                'T{0:g}'.format(T),
                                                'scripts',
                                                'batch',
                                                'N{0:g}_T{1:g}_R{2:g}_hyst.bat'.format(N_hole,
                                                                                T,
                                                                                R_holes*1000))
            with open (batch_script_path, 'w') as f:
                for size in sizes:
                    hyst_dir = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'scripts',
                                            'hysteresis',
                                            str(size))
                    for file in os.listdir(hyst_dir):
                        filepath = os.path.join(hyst_dir, file)
                        f.write('merrill {} \n'.format(filepath))

def create_size_hysteresis_scripts_up(geometry, N_holes, Ts, sizes, R_holes):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            for size in sizes:
                patran_path = os.path.join(base,
                                          '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                          'T{0:g}'.format(T),
                                          'patran',
                                          's{0:g}_N{1:g}_T{2:g}_R{3:g}.pat'.format(size, N_hole, T, R_holes*1000))
                patran_path = "/" + "/".join(patran_path.split('\\')[1:])
                
                groundstates_script_path = os.path.join(base,
                                                    '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                                    'T{0:g}'.format(T),
                                                    'scripts',
                                                    'size_hysteresis',
                                                    's{0:g}_N{1:g}_T{2:g}_R{3:g}_up'.format(size, N_hole, T, R_holes*1000))
                groundstates_script_path = "/" + "/".join(groundstates_script_path.split('\\')[1:])
                with open(groundstates_script_path, 'w') as f:                    
                    f.write(" \n")
                    f.write("Set MaxMeshNumber 1 \n")
                    f.write("Set MaxEnergyEvaluations 10000 \n")
                    f.write("ReadMesh 1 {} \n".format(patran_path))
                    f.write("Magnetite {0:g} C \n".format(T))
                    f.write(" \n")
                    f.write("Uniform Magnetization 1 1 1.0001 \n")
                    f.write("Randomize Magnetization 10 \n")
                    el_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'energylog',
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_up'.format(size, N_hole, T, R_holes*1000))
                    el_path = "/" + "/".join(el_path.split('\\')[1:])
                    f.write("Energylog {} \n".format(el_path))
                    f.write("Minimize \n")
                    sols_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'hysteresis',
                                            'size_loop',
                                            'states',
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_up'.format(size, N_hole, T, R_holes*1000))
                    sols_path = "/" + "/".join(sols_path.split('\\')[1:])
                    f.write("WriteMagnetization {}  \n".format(sols_path))
                    hyst_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'hysteresis',
                                            'size_loop',
                                            'hyst',
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_up'.format(size, N_hole, T, R_holes*1000))
                    hyst_path = "/" + "/".join(hyst_path.split('\\')[1:])
                    f.write("WriteHyst {} \n".format(hyst_path))
                    f.write("CloseLogFile \n")                            
                    f.write(" \n")                        
                    
def create_batch_script_size_hysteresis_up(geometry, N_holes, Ts, sizes, R_holes):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            mscripts_dir = os.path.join(base,
                                        '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                        'T{0:g}'.format(T),
                                        'scripts',
                                        'size_hysteresis')
            batch_script_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'scripts',
                                            'batch',
                                            'N{0:g}_T{1:g}_R{2:g}_up.bat'.format(N_hole, T, R_holes*1000))
            with open(batch_script_path, 'w') as f:
                for file in os.listdir(mscripts_dir):
                    if 'up' in file:
                        filepath = os.path.join(mscripts_dir, file)
                        f.write('merrill {} \n'.format(filepath))
    
def create_size_hysteresis_scripts_down(geometry, N_holes, Ts, sizes, R_holes):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            for size in sizes:
                patran_path = os.path.join(base,
                                          '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                          'T{0:g}'.format(T),
                                          'patran',
                                          's{0:g}_N{1:g}_T{2:g}_R{3:g}.pat'.format(size, N_hole, T, R_holes*1000))
                patran_path = "/" + "/".join(patran_path.split('\\')[1:])
                
                groundstates_script_path = os.path.join(base,
                                                    '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                                    'T{0:g}'.format(T),
                                                    'scripts',
                                                    'size_hysteresis',
                                                    's{0:g}_N{1:g}_T{2:g}_R{3:g}_down'.format(size, N_hole, T, R_holes*1000))
                groundstates_script_path = "/" + "/".join(groundstates_script_path.split('\\')[1:])
                with open(groundstates_script_path, 'w') as f:                    
                    f.write(" \n")
                    f.write("Set MaxMeshNumber 1 \n")
                    f.write("Set MaxEnergyEvaluations 10000 \n")
                    f.write("ReadMesh 1 {} \n".format(patran_path))
                    f.write("Magnetite {0:g} C \n".format(T))
                    f.write(" \n")
                    f.write("Vortex 0 0 1.0001 0.002 LH \n")
                    f.write("Randomize Magnetization 10 \n")
                    el_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'energylog',
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_down'.format(size, N_hole, T, R_holes*1000))
                    el_path = "/" + "/".join(el_path.split('\\')[1:])
                    f.write("Energylog {} \n".format(el_path))
                    f.write("Minimize \n")
                    sols_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'hysteresis',
                                            'size_loop',
                                            'states',
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_down'.format(size, N_hole, T, R_holes*1000))
                    sols_path = "/" + "/".join(sols_path.split('\\')[1:])
                    f.write("WriteMagnetization {}  \n".format(sols_path))
                    hyst_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'hysteresis',
                                            'size_loop',
                                            'hyst',
                                            's{0:g}_N{1:g}_T{2:g}_R{3:g}_down'.format(size, N_hole, T, R_holes*1000))
                    hyst_path = "/" + "/".join(hyst_path.split('\\')[1:])
                    f.write("WriteHyst {} \n".format(hyst_path))
                    f.write("CloseLogFile \n")                            
                    f.write(" \n")
                    
def create_batch_script_size_hysteresis_down(geometry, N_holes, Ts, sizes, R_holes):
    base = create_base_directory(geometry)
    for N_hole in N_holes:
        for T in Ts:
            mscripts_dir = os.path.join(base,
                                        '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                        'T{0:g}'.format(T),
                                        'scripts',
                                        'size_hysteresis')
            batch_script_path = os.path.join(base,
                                            '{0:g}_holes_R{1:g}'.format(N_hole, R_holes*1000),
                                            'T{0:g}'.format(T),
                                            'scripts',
                                            'batch',
                                            'N{0:g}_T{1:g}_R{2:g}_down.bat'.format(N_hole, T, R_holes*1000))
            with open(batch_script_path, 'w') as f:
                for file in os.listdir(mscripts_dir):
                    if 'down' in file:
                        filepath = os.path.join(mscripts_dir, file)
                        f.write('merrill {} \n'.format(filepath))
                        
