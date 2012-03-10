# encoding: utf-8

from dfa_common import run_cmd


def install_dwarf_therapist(): #{{{
        """ Install Dwarf Therapist (Ubuntu) """

        sources_path = '/etc/apt/sources.list'
        sources = open(sources_path).readlines()
        dt_lines = [line for line in sources
                if 'dwarftherapist.com/apt' in line]

        if len(dt_lines) == 0:
            print 'Dwarf Therapist repo not found in {sources}'.format(
                    sources=sources_path)
            print 'Adding repo to {sources}'.format(sources=sources_path)

            run_cmd("sudo apt-add-repository " +
                    "'deb http://dwarftherapist.com/apt oneiric universe'")
        else:
            print 'Dwarf Therapist found in {sources}, not adding.'.format(
                    sources=sources_path)

        run_cmd("sudo apt-get update")
        run_cmd("sudo apt-get install dwarftherapist") #}}}
