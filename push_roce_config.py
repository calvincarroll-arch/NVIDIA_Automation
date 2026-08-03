from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_jinja2.plugins.tasks import template_file
import os

def push_lossless_qos(task: Task) -> Result:
    # Render the Jinja2 template using host-specific data from NetBox
    rendered = task.run(
        task=template_file,
        template="roce_qos.j2",
        path="day1_provisioning/templates"
    )
    task.host["rendered_config"] = rendered.result
    
    return Result(host=task.host, result=f"Successfully generated and staged RoCEv2 QoS config for {task.host.name}\n{task.host['rendered_config']}")

def main():
    # Initialize Nornir using your NetBox inventory config
    nr = InitNornir(config_file="day1_provisioning/inventory/config.yaml")
    
    print("--- IRON LOGIC: PUSHING ROCEv2 INTENT CONFIGS ---")
    results = nr.run(task=push_lossless_qos)
    
    # Check if inventory is empty
    if not nr.inventory.hosts:
        print("[WARNING] No devices found in NetBox inventory. Please add devices to NetBox first.")
        return

    for host, result in results.items():
        print(f"\n[SUCCESS] {host}:")
        print(result[0].result)

if __name__ == "__main__":
    main()