import os
import subprocess
import sys
# Set the path to the OVA and the ovftool executable
ova_path = sys.argv[1]
ovftool_path = "ovftool"

# Convert the OVA to OVF
ovf_path = ova_path.replace(".ova", ".ovf")
subprocess.call([ovftool_path, ova_path, ovf_path])

# Remove the ovf:key="guestinfo.cis.deployment.autoconfig" property from the OVF
with open(ovf_path, "r+b") as ovf_file:
    ovf_data = ovf_file.read()
    ovf_file.seek(0)
    ovf_file.truncate()
    ovf_file.write(ovf_data.replace(b'ovf:key="guestinfo.cis.deployment.autoconfig" ovf:type="boolean" ovf:userConfigurable="false" ovf:value="False"', b'ovf:key="guestinfo.cis.deployment.autoconfig" ovf:type="boolean" ovf:userConfigurable="false" ovf:value="True"'))


# Delete the manifest file
#manifest_path = ovf_path + ".mf"
#if os.path.exists(manifest_path):
#    os.remove(manifest_path)

os.remove(ova_path.replace(".ova", ".mf"))

# Convert the OVF back to OVA
new_ova_path = ova_path.replace(".ova", "_mod.ova")
subprocess.call([ovftool_path, ovf_path, new_ova_path])

# Delete the manifest file
#manifest_path = ovf_path + ".mf"
#if os.path.exists(manifest_path):
#    os.remove(manifest_path)


# Remove the intermediate OVF file
os.remove(ovf_path)
