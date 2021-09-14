#!/usr/bin/env python3
import os
import base64
import time

import yaml
import sys

from jinja2 import Template

from dialog import Dialog

from templates.available import SWITCH_FLAGS


def get_random_prefix(size=8):
    rand_bytes = os.urandom(size)
    rand_str = base64.b64encode(rand_bytes).decode('ascii')
    rand_str = rand_str.replace("+", "_")
    rand_str = rand_str.replace("/", "_")
    rand_str = rand_str.split('=', 1)[0]
    return rand_str


def switch_flags_menu(d):
    menu_options = []
    for flag_var, flag_meta in SWITCH_FLAGS.items():
        menu_options.append((flag_meta['var_name'], flag_meta['help'], False))
    selected_switches = d.checklist(
        ("Select optional 'switch flags' to include. Switch flags essentially"
         " enable a feature if they are present."),
        choices=menu_options,
        width=60,
    )
    return selected_switches


client_specs = {}

def load_client_spec_yamls():
    client_choices_menu = []
    base_dir = "client_specs"
    files = os.listdir(base_dir)
    yaml_files = [f for f in files if f.endswith(".yml") or f.endswith(".yaml")]

    for yaml_file in yaml_files:
        yaml_path = os.path.join(base_dir, yaml_file)
        with open(yaml_path, "r") as yaml_file_obj:
            info = yaml.load(yaml_file_obj, Loader=yaml.Loader)
            client_specs[info['short_name']] = info

        client_choices_menu.append(
            (info['short_name'], info['description'], False, )
        )

    return client_choices_menu


def main():
    d = Dialog(dialog="dialog")
    main_args = []  # Args that will go into generated scripts' main()
                    # signature

    client_choices_menu = load_client_spec_yamls()
    status, selected_clients = d.checklist(
        ("Select API Clients to add to the generated script."),
        choices=client_choices_menu,
        width=70,
    )

    # These will generate the options in click script.
    client_args_list = []

    if status != 'ok':
        print("\nAborted\n")
        sys.exit(0)

    instance_templates = []
    for client in selected_clients:
        current_client = client_specs[client]  # by shortname
        if "instance_template" in current_client:
            instance_templates.append(current_client['instance_template'])
        option_varnames = [opt['varname'] for opt in current_client['options']]
        main_args.extend(option_varnames)
        client_args_list.extend(current_client['options'])

    # Get prefix for all environment variables
    status, entered_prefix = d.inputbox(
        "Environment variables prefix",
        init=get_random_prefix()
    )

    status, chosen_switches = switch_flags_menu(d)

    if status != 'ok':
        print("\nAborted\n")
        sys.exit(0)

    switch_flags = [SWITCH_FLAGS[switch] for switch in chosen_switches]
    main_args.extend(chosen_switches)
    switches_template = Template(
        open('templates/click_option_switch_flag.j2', 'r').read().strip(),
    )

    main_args_string = ", ".join(main_args)
    output = switches_template.render(
        switch_flags=switch_flags,
        main_args=main_args,
        instance_templates=instance_templates,
        prefix=entered_prefix,
        client_args_list=client_args_list,
    )

    with open("final_script.py", "w") as output_script:
        output_script.write(output)

if __name__ == "__main__":
    main()
