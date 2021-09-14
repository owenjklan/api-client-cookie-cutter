#!/usr/bin/env python3

import click


# LogicMonitor hostname template
LM_INSTANCE_HOST = "{lm_instance_id}.logicmonitor.com"


@click.command()

@click.option("--lm-instance-id", "lm_instance_id",
              envvar="wi9JdK0fOLk_LM_INSTANCE",
              type=str,
              help="Specify the LogicMonitor instance to operate with.")
@click.option("--lm-access-id", "lm_access_id",
              envvar="wi9JdK0fOLk_LM_ACCESS_ID",
              type=str,
              help="Specify AccessID to use with LogicMonitor REST APIs.")
@click.option("--lm-access-key", "lm_access_key",
              envvar="wi9JdK0fOLk_LM_ACCESS_KEY",
              type=str,
              help="Specify Access Key for associated AccessID.")
@click.option("--debug", "debug_flag",
              type=bool, is_flag=True,
              default=False, show_default=False,
              help=("Add more debugging output"))
def main(lm_instance_id, lm_access_id, lm_access_key, debug_flag):
    lm_instance_host = LM_INSTANCE_HOST.format(lm_instance_id=lm_instance_id)

    print("Hello there")


if __name__ == "__main__":
    main()