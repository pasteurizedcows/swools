'''
This class is to read and write the OPTIONS portion of the SWMM .inp file
'''

from swool_utilities import flt_int

class Options(object):
    '''
    The OPTIONS class from the SWMM .inp file
    '''

    def __init__(self):
        self.flow_units = None
        self.infiltration = None
        self.flow_routing = None
        self.link_offsets = None
        self.min_slope = None
        self.allow_ponding = None
        self.skip_steady_state = None
        self.start_date = None
        self.start_time = None
        self.report_start_date = None
        self.report_start_time = None
        self.end_date = None
        self.end_time = None
        self.sweep_start = None
        self.sweep_end = None
        self.dry_days = None
        self.report_step = None
        self.wet_step = None
        self.dry_step = None
        self.routing_step = None
        self.rule_step = None
        self.intertial_damping = None
        self.normal_flow_ltd = None
        self.force_main_eq = None
        self.variable_step = None
        self.lengthening_step = None
        self.min_surfarea = None
        self.max_trials = None
        self.head_tolerance = None
        self.sys_flow_tol = None
        self.lat_flow_tol = None
        self.minimum_step = None
        self.threads = None

    def __str__(self):
        # since keys are kept in the same order as their insertion/creation
        # in dictionaries, the keys will be used in the following order when
        # writing the class' string
        params_values = {'FLOW_UNITS' : self.flow_units,
                        'INFILTRATION' : self.infiltration,
                        'FLOW_ROUTING' : self.flow_routing,
                        'LINK_OFFSETS' : self.link_offsets,
                        'MIN_SLOPE' : self.min_slope,
                        'ALLOW_PONDING' : self.allow_ponding,
                        'SKIP_STEADY_STATE' : self.skip_steady_state,
                        'START_DATE' : self.start_date,
                        'START_TIME' : self.start_time,
                        'REPORT_START_DATE' : self.report_start_date,
                        'REPORT_START_TIME' : self.report_start_time,
                        'END_DATE' : self.end_date,
                        'END_TIME' : self.end_time,
                        'SWEEP_START' : self.sweep_start,
                        'SWEEP_END' : self.sweep_end,
                        'DRY_DAYS' : self.dry_days,
                        'REPORT_STEP' : self.report_step,
                        'WET_STEP' : self.wet_step,
                        'DRY_STEP' : self.dry_step,
                        'ROUTING_STEP' : self.routing_step,
                        'RULE_STEP' : self.rule_step,
                        'INERTIAL_DAMPING' : self.intertial_damping,
                        'NORMAL_FLOW_LIMITED' : self.normal_flow_ltd,
                        'FORCE_MAIN_EQUATION' : self.force_main_eq,
                        'VARIABLE_STEP' : self.variable_step,
                        'LENGTHENING_STEP' : self.lengthening_step,
                        'MIN_SURFAREA' : self.min_surfarea,
                        'MAX_TRIALS' : self.max_trials,
                        'HEAD_TOLERANCE' : self.head_tolerance,
                        'SYS_FLOW_TOL' : self.sys_flow_tol,
                        'LAT_FLOW_TOL' : self.lat_flow_tol,
                        'MINIMUM_STEP' : self.minimum_step,
                        'THREADS' : self.threads}

        s = '[OPTIONS]\n'
        s += ';;Options            Value\n'
        s +=  ';;------------------ ------------\n'
        for k, v in params_values.items():
            if v is not None:
                s += k.ljust(21)
                s += str(v)
                s += '\n'
            else:
                pass
        s += '\n'
        return s

    @staticmethod
    def has_reached_section(line):
        '''
        Determines if the OPTIONS section has been reached when reading the
        .inp file

        Parameters
        ----------
        line : str
            current line from the .inp file

        Returns
        -------
        bool
            True if [OPTIONS], else False
        '''
        if line.strip() == '[OPTIONS]':
            return True
        else:
            return False

    def read_params(self, inp_file):
        '''
        Reads the OPTIONS parameters from the .inp file and records them
        as attributes

        Parameters
        ----------
        inp_file : input file
            the SWMM .inp file

        Returns
        -------
        str
            the line after the last param
        '''

        # the cutoff to stop reading the params is a new line
        # skip the first two lines
        first_lines_flag = True
        for line in inp_file:
            if first_lines_flag is True:
                line = next(inp_file)
                line = next(inp_file)
                first_lines_flag = False

            if line != '\n':
                temp = line.split()
                param = temp[0].strip()
                value = temp[1].strip()

                if param == 'FLOW_UNITS':
                    self.flow_units = value
                elif param == 'INFILTRATION':
                    self.infiltration = value
                elif param == 'FLOW_ROUTING':
                    self.flow_routing = value
                elif param == 'LINK_OFFSETS':
                    self.link_offsets = value
                elif param == 'MIN_SLOPE':
                    self.min_slope = flt_int(value)
                elif param == 'ALLOW_PONDING':
                    self.allow_ponding = value
                elif param == 'SKIP_STEADY_STATE':
                    self.skip_steady_state = value
                elif param == 'START_DATE':
                    self.start_date = value
                elif param == 'START_TIME':
                    self.start_time = value
                elif param == 'REPORT_START_DATE':
                    self.report_start_date = value
                elif param == 'REPORT_START_TIME':
                    self.report_start_time = value
                elif param == 'END_DATE':
                    self.end_date = value
                elif param == 'END_TIME':
                    self.end_time = value
                elif param == 'SWEEP_START':
                    self.sweep_start = value
                elif param == 'SWEEP_END':
                    self.sweep_end = value
                elif param == 'DRY_DAYS':
                    self.dry_days = flt_int(value)
                elif param == 'REPORT_STEP':
                    self.report_step = value
                elif param == 'WET_STEP':
                    self.wet_step = value
                elif param == 'DRY_STEP':
                    self.dry_step = value
                elif param == 'ROUTING_STEP':
                    self.routing_step = flt_int(value)
                elif param == 'RULE_STEP':
                    self.rule_step = value
                elif param == 'INERTIAL_DAMPING':
                    self.intertial_damping = value
                elif param == 'NORMAL_FLOW_LIMITED':
                    self.normal_flow_ltd = value
                elif param == 'FORCE_MAIN_EQUATION':
                    self.force_main_eq = value
                elif param == 'VARIABLE_STEP':
                    self.variable_step = flt_int(value)
                elif param == 'LENGTHENING_STEP':
                    self.lengthening_step = flt_int(value)
                elif param == 'MIN_SURFAREA':
                    self.min_surfarea = flt_int(value)
                elif param == 'MAX_TRIALS':
                    self.max_trials = flt_int(value)
                elif param == 'HEAD_TOLERANCE':
                    self.head_tolerance = flt_int(value)
                elif param == 'SYS_FLOW_TOL':
                    self.sys_flow_tol = flt_int(value)
                elif param == 'LAT_FLOW_TOL':
                    self.lat_flow_tol = flt_int(value)
                elif param == 'MINIMUM_STEP':
                    self.minimum_step = flt_int(value)
                elif param == 'THREADS':
                    self.threads = flt_int(value)
                else:
                    raise Exception('{} is missing from Options.read_params'.format(param))
            else:
                break

        return line

if __name__ == '__main__':

    test = Options()
    print(isinstance(test, Options))

    '''
    from pathlib import Path
    import difflib

    home_dir = Path('C:/C_PROJECTS/Python/swools')
    test_dir = home_dir / 'tests' / 'options_tests'

    # test 1
    options_1 = Options()

    test_1_file = test_dir / 'options_1.inp'
    with open(test_1_file, 'r') as test_1:
        for line in test_1:
            if Options.has_reached_section(line):
                line = options_1.read_params(test_1)

    out_1 = test_dir / 'outputs' / 'out_1.inp'
    with open(out_1, 'w') as out_file:
        out_file.write(str(options_1))

    t1 = open(test_1_file)
    t2 = open(out_1)
    diff = difflib.ndiff(t1.readlines(), t2.readlines())
    for l in diff:
        print(l)

    # test 2

    options_2 = Options()
    test_2_file = test_dir / 'options_2.inp'
    with open(test_2_file, 'r') as test_2:
        for line in test_2:
            if Options.has_reached_section(line):
                print('hooray')
                line = options_2.read_params(test_2)

    out_2 = test_dir / 'outputs' / 'out_2.inp'
    with open(out_2, 'w') as out_file:
        out_file.write(str(options_2))

    t1 = open(test_2_file)
    t2 = open(out_2)
    diff = difflib.ndiff(t1.readlines(), t2.readlines())
    for l in diff:
        print(l)
    '''
