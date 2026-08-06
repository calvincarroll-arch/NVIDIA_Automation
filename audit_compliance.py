import sys
from deepdiff import DeepDiff
from nornir import InitNornir
from jinja2 import Environment, FileSystemLoader

# 1. Setup Jinja2 template loader pointing to your templates directory
file_loader = FileSystemLoader('day1_provisioning/templates')
env = Environment(loader=file_loader)

def audit_switch_compliance(task):
    """
    Parses simulated live state vs golden Jinja2 baseline to detect configuration drift.
    """
    # Load and render golden intent using host context from NetBox
    template = env.get_template('roce_qos.j2')
    
    # Context data for rendering Jinja2 template
    context = {
        'host': task.host,
        'asn': task.host.get('asn', '65000'),
        'router_id': task.host.get('primary_ip', '10.255.0.1')
    }
    
    golden_rendered = template.render(context)
    
    # Structuring golden intent for comparison
    golden_intent = {
        "qos_enabled": True,
        "ecn_min_th": 150,
        "ecn_max_th": 350,
        "pfc_queue": 3
    }
    
    # Simulate live running state from switch
    running_state = golden_intent.copy()
    
    # Introduce deliberate drift on atl-ept-lf-05 to test the detector
    if task.host.name == "atl-ept-lf-05":
        running_state["ecn_max_th"] = 400  # Drift!

    # Calculate structural difference
    diff = DeepDiff(golden_intent, running_state, ignore_order=True)

    if not diff:
        print(f"✅ [COMPLIANT] {task.host.name}: Running state matches Golden Baseline 100%.")
    else:
        print(f"⚠️  [NON-COMPLIANT DRIFT DETECTED] {task.host.name}:")
        print(diff.pretty())

def main():
    print("--- IRON LOGIC: PRE/POST-CHANGE COMPLIANCE AUDITOR ---\n")
    nr = InitNornir(config_file="day1_provisioning/inventory/config.yaml")
    nr.run(task=audit_switch_compliance)

if __name__ == "__main__":
    main()