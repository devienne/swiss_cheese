
import os

def create_base_directory(geometry):
    root = os.getcwd()
    geometry_dir = os.path.join(root, geometry)
    if not os.path.isdir(geometry_dir):
        os.mkdir(geometry_dir)
        return geometry_dir
    else:
        return geometry_dir

def create_holes_directories(base, N_roles):
    N_roles_dir_name = '{}_roles'.format(N_roles)
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
                        
def create_all_directories(geometry, N_roles, Ts, sizes):
    base = create_base_directory(geometry)
    for N_role in N_roles:
        for T in Ts:
            hole_dir = create_holes_directories(base, N_role)
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
