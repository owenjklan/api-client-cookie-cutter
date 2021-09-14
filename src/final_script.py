#!/usr/bin/env python3
import click


# LogicMonitor hostname template
LM_INSTANCE_HOST = "{lm_instance_id}.logicmonitor.com"


@click.command()
@click.option("--lm-instance-id", "lm_instance_id",
              envvar="eJ_LM_INSTANCE",
              type=str, metavar="INSTANCE",
              help="Specify the LogicMonitor instance to operate with. Eg: 'equate'")
@click.option("--lm-access-id", "lm_access_id",
              envvar="eJ_LM_ACCESS_ID",
              type=str, metavar="ACCESS_ID",
              help="Specify AccessID to use with LogicMonitor REST APIs.")
@click.option("--lm-access-key", "lm_access_key",
              envvar="eJ_LM_ACCESS_KEY",
              type=str, metavar="ACCESS_KEY",
              help="Specify Access Key for associated AccessID.")
@click.option("--nucleus-project-id", "nucleus_project_id",
              envvar="eJ_NUCLEUS_PROJECT",
              type=int, metavar="PROJECT_ID",
              help="Specify the LogicMonitor instance to operate with.")
@click.option("--nucleus-api-key", "nucleus_api_key",
              envvar="eJ_NUCLEUS_API_KEY",
              type=str, metavar="API_KEY",
              help="Specify API Key to use with Nucleus REST APIs.")

@click.option("--debug", "debug_flag",
              type=bool, is_flag=True,
              default=False, show_default=False,
              help=("Add more debugging output"))
@click.option("--verbose", "verbose_flag",
              type=bool, is_flag=True,
              default=False, show_default=False,
              help=("Be more verbose in output"))
@click.option("--quiet", "quiet_flag",
              type=bool, is_flag=True,
              default=False, show_default=False,
              help=("Reduce output, ideal for scripts"))
def main(lm_instance_id, lm_access_id, lm_access_key, nucleus_project_id, nucleus_api_key, debug_flag, verbose_flag, quiet_flag):
    """
    
    

    Auto-generated Click Cookie-Cutter Script
    """
    lm_instance_host = LM_INSTANCE_HOST.format(lm_instance_id=lm_instance_id)

    print("Hello there")


if __name__ == "__main__":
    main()