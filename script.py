import tss_cmd


tss_cmd.api.login("", "")
print(tss_cmd.server.run_command("tree"))
