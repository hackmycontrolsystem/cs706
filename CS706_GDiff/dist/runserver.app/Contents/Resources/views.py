# DO NOT TOUCH
from flask import Flask, url_for, request, render_template, Response;
#import runserver variable from runserver.py file
from StructOpt import app;
from _ctypes import Structure
from fileinput import filename
import os
import sys
import jinja2.ext
import logging

from flask.globals import request
import paramiko


app = Flask(__name__)


# our code - Server side
#def resource_path(relative):
#    if hasattr(sys, "_MEIPASS"):
#        return os.path.join(sys._MEIPASS, relative)
#    return os.path.join(relative)

#if getattr(sys, 'frozen'):
#    here = sys.executable
#else:
 #   here = os.path.realpath(__file__)
    
#server
@app.route('/StructOpt', methods = ['GET', 'POST'])
def StructOpt():
    if request.method == 'GET':
        # send user the form
        print("in render template2", sys.path.append(os.getcwd()));
        try:
            render_template("parameters.html");
        except Exception as e:
            logging.exception('Error: %s', e)
        return render_template("parameters.html");
    elif request.method == 'POST':
        print(request.form)
        # read the form data and save it
        structure = request.form['structure'];
        seed = request.form['seed'];
        nindiv = request.form['nindiv'];
        fixed_region = request.form['fixed_region']
        fingerprinting = request.form['fingerprinting'];
        fpbin = request.form['fpbin'];
        number_of_bests = request.form['number_of_bests'];
        migration_percent = request.form['migration_percent'];
        constrain_position = request.form['constrain_position'];
        filename_var = request.form['filename'];
        systemname_var = request.form['systemname'];
        vacancy_output = request.form['vacancy_output'];
        restart = request.form['restart'];
        indiv_defect_write = request.form['indiv_defect_write'];
        forcing = request.form['forcing'];
        migration_intervals = request.form['migration_intervals'];
        fpcutoff = request.form['fpcutoff'];
        #natoms = request.form['natoms'];
        r_ab = request.form['r_ab'];
        output_format = request.form['output_format'];
        algorithm_type = request.form['algorithm_type'];
        best_inds_list = request.form['best_inds_list'];
        allenergyfile = request.form['allenergyfile'];
        genealogy = request.form['genealogy'];
        rattle_atoms = request.form['rattle_atoms'];
        size_pop = request.form['size_pop'];
        parallel = request.form['parallel'];
        structure = request.form['structure'];
        lattice_concentration = request.form['lattice_concentration'];
        genealogytree = request.form['genealogytree'];
        generate_flag = request.form['generate_flag'];
        restart_ints = request.form['restart_ints'];
        postprocessing = request.form['postprocessing'];
        debug = request.form['debug'];
        optimizer_type = request.form['optimizer_type'];
        atomList_values = request.form['atomList_values'];
        atomlist = "";
        natoms=0;
        for i in range(0,int(atomList_values)):
            atomlist += "('";
            atomlist += request.form['type_atom'+str(i)] + "',";
            atomlist += request.form['concentration_atom'+str(i)] + ",";
            atomlist += request.form['mass_atom'+str(i)] + ",";
            atomlist += request.form['potential_atom'+str(i)];
            atomlist += "),";
            natoms = natoms + int(request.form['concentration_atom'+str(i)])
        calc_method = request.form['calc_method'];
        vaspcalc = request.form['vaspcalc'];
        pair_style = request.form['pair_style'];
        bopcutoff = request.form['bopcutoff'];
        buckcutoff = request.form['buckcutoff'];
        buckparameters = request.form['buckparameters'];
        ps_other = request.form['ps_other'];
        ps_name = request.form['ps_name'];
        pair_coeff = request.form['pair_coeff'];
        pot_file = "/home/usitguest/USIT/dropbox_app/potentialFile.txt"; #request.form['pot_file'];
        lammps_keep_files = request.form['lammps_keep_files'];
        lammps_min = request.form['lammps_min'];
        lammps_min_style = request.form['lammps_min_style'];
        lammps_thermo_steps = request.form['lammps_thermo_steps'];
        ase_min = "false"; #request.form['ase_min'];
        ase_min_fmax = 0.01; #request.form['ase_min_fmax'];
        ase_min_maxsteps = 2500; #request.form['ase_min_maxsteps'];
        large_box_size = request.form['large_box_size'];
        energy_cutoff_factor = request.form['energy_cutoff_factor'];
        cxpb = request.form['cxpb'];
        cx_scheme = request.form['cx_scheme'];
        mutpb = request.form['mutpb'];
        mutant_add = request.form['mutant_add'];
        mutation_options = request.form['mutation_options_text'];
        selection_scheme = request.form['selection_scheme'];
        natural_selection_scheme = request.form['natural_selection_scheme'];
        fitness_scheme = request.form['fitness_scheme'];
        convergence_scheme = request.form['convergence_scheme'];
        predator = request.form['predator'];
        demin = request.form['demin'];
        potentialFileContent = request.form['potentialFileContent'];
        solidFileContent = request.form['solidFileContent'];
        emailAddress = request.form['emailAddress'];
        
        if (structure == "Defect"):
            sf = request.form['sf'];
            supercell_x = request.form['supercell_x0'];
            supercell_y = request.form['supercell_y0'];
            supercell_z = request.form['supercell_z0'];
            solidfile = "/home/usitguest/USIT/dropbox_app/solidFile.txt"; #request.form['solidfile'];
            solidcell_x = request.form['solidcell_x0'];
            solidcell_y = request.form['solidcell_y0'];
            solidcell_z = request.form['solidcell_z0'];
            evalsolid = request.form['evalsolid'];
            finddefects = request.form['finddefects'];
            trackvacs = request.form['trackvacs'];
            trackswaps = request.form['trackswaps'];
            alloy = request.form['alloy'];
            random_vac_start = request.form['random_vac_start'];
            random_loc_start = request.form['random_loc_start'];
            
        if(structure == "Cluster"):
            cell_shape_options = request.form['cell_shape_options_text'];
            
        inputContent = "structure " + structure + "\n" + "optimizer_type " + optimizer_type + "\n" + "filename " + filename_var + "\n" + "atomlist [" + atomlist[0:-1] + "]\n" + "algorithm_type " + algorithm_type + "\n" +"natoms " + str(natoms) + "\n" + "nindiv " + nindiv + "\n" + "r_ab " + r_ab + "\n" +"size " + size_pop + "\n" + "indiv_defect_write " + indiv_defect_write + "\n" + "cxpb " + cxpb + "\n" +"mutpb "  + mutpb + "\n" + "cx_scheme " + cx_scheme + "\n" + "fitness_scheme " + fitness_scheme + "\n" + "selection_scheme " + selection_scheme + "\n" + "natural_selection_scheme " + natural_selection_scheme + "\n" + "convergence_scheme " + convergence_scheme + "\n" +"predator " + predator + "\n" + "demin " + demin + "\n" + "mutant_add " + mutant_add + "\n" + "mutation_options [" + mutation_options[0:-1] + "]\n" + "forcing " + forcing + "\n" + "calc_method " + calc_method + "\n" + "pair_style " + pair_style + "\n" + "pot_file " + pot_file + "\n" + "lammps_keep_files " + lammps_keep_files + "\n" + "ase_min " + ase_min + "\n" +"lammps_min " + lammps_min + "\n" + "lammps_min_style " + lammps_min_style + "\n" + "genealogy " + genealogy + "\n" + "output_format " + output_format + "\n" + "allenergyfile " + allenergyfile + "\n" + "best_inds_list " + best_inds_list + "\n" + "latticeconcentration " + lattice_concentration + "\n" + "debug ['" + debug + "']\n";
                        
        if (structure == "Defect"):
            inputContent +=   "sf " + sf + "\n" + "supercell (" + supercell_x + "," + supercell_y + "," + supercell_z + ")\n" +"solidfile " + solidfile + "\n" + "solidcell (" + solidcell_x + "," + solidcell_y + "," + solidcell_z + ")\n" + "evalsolid " + evalsolid + "\n" + "finddefects " + finddefects + "\n" +"alloy " + alloy + "\n" + "random_loc_start " + random_loc_start + "\n" + "trackvacs " + trackvacs + "\n" +"trackswaps " + trackswaps + "\n" + "random_vac_start " + random_vac_start  + "\n";
                        
        if(structure == "Cluster"):
            inputContent += "cell_shape_options [" + cell_shape_options[0:-1] + "]\n";               
        
        if(convergence_scheme == "max_gen"):
            maxgen = request.form['maxgen'];
            inputContent += "maxgen "+ maxgen + "\n";
        elif (convergence_scheme == "gen_rep_min" or convergence_scheme == "gen_rep_avg"):
            reqrep = request.form['reqrep'];
            tolerance = request.form['tolerance'];
            inputContent += "reqrep "+ reqrep + "\n" + "tolerance " + tolerance + "\n";
        if(natural_selection_scheme == "fuss" or
                    natural_selection_scheme == "fuss" or
                    natural_selection_scheme == "fuss1" or
                    natural_selection_scheme == "fuss1r" or
                    natural_selection_scheme == "fuss2" or
                    natural_selection_scheme == "fussf" or
                    natural_selection_scheme == "fussr"):
            fusslimit = request.form['fusslimit'];
            inputContent += "fusslimit " + fusslimit;
        elif (natural_selection_scheme == "tournament" or
              natural_selection_scheme == "tournament1" or
              natural_selection_scheme == "tournament2"):
            tournsize = request.form['tournsize'];
            inputContent += "tournsize " + tournsize;
        
        if(calc_method == "MAST_VASP"):
            vaspParams = request.form['vaspParams'];
            vaspParamsLines = vaspParams.splitlines();
            vaspParams = "";
            for i in range(0, len(vaspParamsLines)):
                vaspParams += vaspParamsLines[i] +"\n";
            inputContent = "$mast\nsystem_name " + systemname_var + "\n$end\n\n$structure\ncoord_type fractional\n\nbegin elementmap\nX1 Si\nX2 C\nend\n\n#begin lattice and coordinates irrelavent for defect type calc, where initial coordinates (POSCAR) are required to provided.\nbegin lattice\n3.5 0 0\n0 3.5 0\n0 0 3.5\nend\n\nbegin coordinates\nX1 0.0000000000 0.0000000000 0.0000000000\nX1 0.5000000000 0.5000000000 0.0000000000\nX1 0.0000000000 0.5000000000 0.5000000000\nX1 0.5000000000 0.0000000000 0.5000000000\nend\n\n$end\n\n$ingredients\nbegin GAvasp\nmast_nodes 1\nmast_multiplyencut 1.5\nmast_walltime 24\nmast_ppn 16\nmast_queue pre\nmast_exec python /home/hko8/Canopy/appdata/canopy-1.4.1.1975.rh5-x86_64/lib/python2.7/site-packages/MAST-1.2.9.4-py2.7.egg/MAST/structopt/Optimizer.py\nmast_write_method            write_singlerun\nmast_ready_method            ready_singlerun\nmast_run_method              run_singlerun\nmast_complete_method         complete_singlerun\nmast_update_children_method  give_structure\nmast_program   structopt\n\n## INCAR parameters\n" + vaspParams + "\n\n## GA parameters\n" + inputContent;
        elif(calc_method == "MAST_LAMMPS"):
            inputContent = "$mast\nsystem_name " + systemname_var + "\n$end\n\n$structure\ncoord_type fractional\n\nbegin elementmap\nX1 Si\nX2 C\nend\n\n#begin lattice and coordinates irrelavent for defect type calc, where initial coordinates (POSCAR) are required to provided.\nbegin lattice\n3.5 0 0\n0 3.5 0\n0 0 3.5\nend\n\nbegin coordinates\nX1 0.0000000000 0.0000000000 0.0000000000\nX1 0.5000000000 0.5000000000 0.0000000000\nX1 0.0000000000 0.5000000000 0.5000000000\nX1 0.5000000000 0.0000000000 0.5000000000\nend\n\n$end\n\n$ingredients\nbegin GAvasp\nmast_nodes 1\nmast_multiplyencut 1.5\nmast_walltime 24\nmast_ppn 16\nmast_queue pre\nmast_exec python /home/hko8/Canopy/appdata/canopy-1.4.1.1975.rh5-x86_64/lib/python2.7/site-packages/MAST-1.2.9.4-py2.7.egg/MAST/structopt/Optimizer.py\nmast_write_method            write_singlerun\nmast_ready_method            ready_singlerun\nmast_run_method              run_singlerun\nmast_complete_method         complete_singlerun\nmast_update_children_method  give_structure\nmast_program   structopt\n\n## GA parameters\n" + inputContent;
            
        inputContent = inputContent + "\nend\n\n$end\n\n$recipe\nperfect_opt1 (GAvasp)\n$end\n$personal_recipe\nperfect_opt1 (GAvasp)\n$end\n"; 
        generator = (cell for row in inputContent for cell in row)
    
        path = "/Users/mehreenali/Documents/workspace/StructOpt/output"

        if not os.path.exists(path):
            os.makedirs(path)
        
        filename = "input.inp";
        potentialFilename = "potentialFile.txt"
        solidFileNmae="solidFile.txt"
        with open(os.path.join(path, filename), 'wb') as temp_file:
            temp_file.write(inputContent)
            
        with open(os.path.join(path, potentialFilename), 'wb') as temp_file:
            temp_file.write(potentialFileContent.encode('utf-8'))
            
        with open(os.path.join(path, solidFileNmae), 'wb') as temp_file:
            temp_file.write(solidFileContent.encode('utf-8'))
        
        app.config.from_pyfile('config_file.cfg');
            
        ssh = paramiko.SSHClient() ;
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")));
        ssh.connect("bardeen.msae.wisc.edu", username=app.config["BARDEEN_USERNAME"], password= app.config["BARDEEN_PASSWORD"]);
        sftp = ssh.open_sftp()
        
        print(resource_path(os.path.join('output', filename)));
              
        sftp.put(resource_path(os.path.join('output', "input.inp")), "/home/" + app.config["BARDEEN_USERNAME"] + "/USIT/dropbox_app/input.inp")
        
        sftp.put(resource_path(os.path.join('output', "potentialFile.txt")), "/home/" + app.config["BARDEEN_USERNAME"] + "/USIT/dropbox_app/potentialFile.txt")
           
        sftp.put(resource_path(os.path.join('output', "solidFile.txt")), "/home/" + app.config["BARDEEN_USERNAME"] + "/USIT/dropbox_app/solidFile.txt")
            
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd USIT/dropbox_app/ \n ./mast_input_with_email.sh input.inp " + emailAddress)
        
        print("reading outputs from the remote command")
        for l in ssh_stdout :
            print("stdout : %s" % l.strip())
        
        for l in ssh_stderr:
            print("stderr : %s" % l.strip())
    
        sftp.close()
        ssh.close()

        return render_template('success.html'); 

@app.route('/Success', methods = ['GET', 'POST'])
def Success():
    return render_template('parameters.html'); 
