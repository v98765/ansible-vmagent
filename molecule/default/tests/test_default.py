import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("files", [
    "/lib/systemd/system/vmagent.service",
    "/etc/vmagent/vmagent.yml",
    "/usr/local/bin/vmagent-prod"
])

def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file

def test_service(host):
    s = host.service("vmagent")
    # assert s.is_enabled
    assert s.is_running

def test_socket(host):
    s = host.socket("tcp://0.0.0.0:8429")
    assert s.is_listening
