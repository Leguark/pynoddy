"""Package initialization file for pynoddy"""
import os.path
import subprocess


# Import additional modules of pynoddy
from . import history
from history import NoddyHistory
from . import output
from output import NoddyOutput
from output import NoddyTopology

#save this module path for relative paths
package_directory = os.path.dirname(os.path.abspath(__file__))

#paths to noddy & topology executables
noddyPath = os.path.join(package_directory,'../noddy/noddy')
topologyPath = os.path.join(package_directory,'../topology/topology')
=======
# save this module path for relative paths
package_directory = os.path.dirname(os.path.abspath(__file__))

# paths to noddy & topology executables
# noddyPath = os.path.join(package_directory,'../noddy/noddy')
# topologyPath = os.path.join(package_directory,'../topology/topology')
# noddyPath = os.path.join(package_directory, 'noddy/noddy')
# topologyPath = os.path.join(package_directory, 'topology/topology')

# global variables
ensure_discrete_volumes = True  # if True, spatially separated but otherwise
# identical volumes are given separate codes.
null_volume_threshold = 20  # volumes smaller than this are ignored


# completely (as they represent pixelation artefacts).
>>>>>>> refs/remotes/flohorovicic/master

#
# NOTE: check for noddy installation should be performed with unittests!
#
#
# # ensure correct noddy & topology builds are present
# if not os.path.exists(noddyPath) and not os.path.exists(noddyPath + ".exe"):
#     print("Error: could not find a compiled version of noddy at %s. \
#     Please ensure the source has been compiled (using GCC and compile.bat \
#     (windows) or compile.sh (unix))." % noddyPath)
# if not os.path.exists(topologyPath) and not os.path.exists(topologyPath + ".exe"):
#     print("Warning: could not find a compiled version of topology at %s. \
#     Please ensure the source has been compiled (using GCC and compile.bat\
#      (windows) or compile.sh (unix))." % topologyPath)


# Some helper functions are defined directly here:

# Idea to check for program path,
# taken from: http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def compute_model(history, output_name, **kwds):
<<<<<<< HEAD
    import subprocess, os
=======
>>>>>>> refs/remotes/flohorovicic/master
    """Call Noddy and compute the history file

    **Arguments**:
        - *history* = string : filename of history file
        - *output_name* = string : basename for output files

    **Optional Keywords**:
        - *sim_type* = 'BLOCK', 'GEOPHYSICS', 'SURFACES', 'BLOCK_GEOPHYS',
        'TOPOLOGY', 'BLOCK_SURFACES', 'ALL':
            type of Noddy simulation (default: 'BLOCK')
        - *program_name* = string : name of program
            (default: noddy.exe or noddy, both checked)
        - *verbose* = bool: verbose mode, print out information for debugging (default = False)
        - *noddy_path* = path: location of Noddy executable (default: checks environment variable)
    **Returns**:
        -Returns any text outputted by the noddy executable.
    """

    sim_type = kwds.get("sim_type", 'BLOCK')

<<<<<<< HEAD
    out = "Running noddy exectuable at %s(.exe)\n" % noddyPath
    try: #try running .exe file (windows only)
        out +=  subprocess.Popen([noddyPath+".exe", history, output_name, sim_type],
                           shell=False, stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE).stdout.read()
    except OSError: #obviously not running windows - try just the binary
        out +=  subprocess.Popen([noddyPath, history, output_name, sim_type],
                           shell=False, stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE).stdout.read()

    #Thought: Is there any reason compute_topology should not be called here if sim_type == "TOPOLOGY"???
    #It could simplify things a lot....

    return out

def compute_topology(rootname, **kwds):
    import subprocess
    """Call topology to compute the voxel topologies

=======
    # actively select noddy executable
    if "noddy_path" in kwds:
        noddy_path = kwds['noddy_path']
    else:
        np1 = which("noddy")
        np2 = which("noddy.exe")
        if np1 is not None:
            noddy_path = np1
        elif np2 is not None:
            noddy_path = np2
        else:
            raise OSError

    if kwds.has_key("verbose") and kwds['verbose']:
        out = "Running noddy executable at %s(.exe)\n" % noddy_path
    else:
        out = ""
    try:  # try running .exe file (windows only)
        out += subprocess.Popen([noddy_path + ".exe", history, output_name, sim_type],
                                shell=False, stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE).stdout.read()
        subprocess.Popen.communicate()
    except OSError:  # obviously not running windows - try just the binary
        # out += subprocess.Popen([noddy_path, history, output_name, sim_type],
        #                         shell=False, stderr=subprocess.PIPE,
        #                         stdout=subprocess.PIPE).stdout.read()
        p1 = subprocess.Popen([noddy_path, history, output_name, sim_type],
                              shell=False, stdout=subprocess.PIPE)
        subprocess.Popen.wait(p1)

        # out += open(p1.stdout).readlines()

    # Thought: Is there any reason compute_topology should not be called here if sim_type == "TOPOLOGY"???
    # It could simplify things a lot....

    return out


def compute_topology(rootname, **kwds):
    """Call the topology executable to compute a models topology.

>>>>>>> refs/remotes/flohorovicic/master
    **Arguments**:
        - *rootname* = string : rootname of the noddy model to calculate topology for
    **Optional Keywords**:
        - *ensure_discrete_volumes* = True if topological units are broken down into
          separate, spatially continuous volumes. Otherwise
          some topological units may represent two separate
          rock volumes (eg. if a folded unit has been truncated
          by an unconformity). Default is True, though this is
          a global variable (pynoddy.ensure_discrete_volumes)
          so it can be changed during runtime.
        - *null_volume_threshold* = The smallest non-null volume. volumes smaller than this are
          ignored by the topology algorithm (as they represent pixelation artefacts).
          The default is 20 voxels, though this is a global variable and can be changed
          with pynoddy.null_volume_threshold.
        - *topology_path* = path: location of executable for topology calculation
    **Returns**
        -Returns any text outputted by the topology executable, including errors.
    """

<<<<<<< HEAD
    dvol = kwds.get('ensure_discrete_volumes',ensure_discrete_volumes)
    nvt =  kwds.get('null_volume_threshold',null_volume_threshold)

    #convert to string
=======
    dvol = kwds.get('ensure_discrete_volumes', ensure_discrete_volumes)
    nvt = kwds.get('null_volume_threshold', null_volume_threshold)

    # actively select noddy executable
    if "topology_path" in kwds:
        topology_path = kwds['topology_path']
    else:
        tp1 = which("topology")
        tp2 = which("topology.exe")
        if tp1 is not None:
            topology_path = tp1
        elif tp2 is not None:
            topology_path = tp2
        else:
            raise OSError

    # convert to string
>>>>>>> refs/remotes/flohorovicic/master
    if dvol:
        dvol = "1"
    else:
<<<<<<< HEAD
        dvol="0"

    out = "Running topology exectuable at %s(.exe)\n" % topologyPath
    try: #try running .exe file (windows only)
        out =  subprocess.Popen([topologyPath+".exe", rootname, dvol, str(nvt)],
                           shell=False, stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE).stdout.read()
    except OSError: #obviously not running windows - try just the binary
        out =  subprocess.Popen([topologyPath, rootname, dvol, str(nvt)],
                           shell=False, stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE).stdout.read()
=======
        dvol = "0"

    out = "Running topology executable at %s(.exe)\n" % topology_path
    try:  # try running .exe file (windows only)
        out = subprocess.Popen([topology_path + ".exe", rootname, dvol, str(nvt)],
                               shell=False, stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE).stdout.read()
    except OSError:  # obviously not running windows - try just the binary
        out = subprocess.Popen([topology_path, rootname, dvol, str(nvt)],
                               shell=False, stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE).stdout.read()
>>>>>>> refs/remotes/flohorovicic/master
    return out
