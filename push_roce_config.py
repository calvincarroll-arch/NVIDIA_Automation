from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result

def push_lossless_qos(task):
    # Render QoS Template
    qos_result = task.run(
        task=template_file,
        template="roce_qos.j2",
        path="day1_provisioning/templates"
    )
    
    # Render BGP Underlay Template
    bgp_result = task.run(
        task=template_file,
        template="bgp_underlay.j2",
        path="day1_provisioning/templates"
    )
    
    return f"Successfully generated QoS and BGP Underlay intent for {task.host.name}\n\n{qos_result.result}\n{bgp_result.result}"

def main():
    nr = InitNornir(config_file="day1_provisioning/inventory/config.yaml")
    
    print("--- IRON LOGIC: PUSHING MULTI-SITE ROCEv2 & BGP INTENT ---")
    results = nr.run(task=push_lossless_qos)
    
    if not nr.inventory.hosts:
        print("[WARNING] No devices found in NetBox inventory.")
        return

    print_result(results)

if __name__ == "__main__":
    main()