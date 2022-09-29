from ast import walk
from distutils.command.bdist import show_formats


first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

global_scope = []

def combine_names(list_a, list_b):
    finished_list = []
    for i in range(len(list_a)):
        new_name = list_a[i] + ' ' + list_b[i]
        finished_list.append(new_name)
    return finished_list

print(combine_names(first_name, last_name))
