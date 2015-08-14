from atomicapp.plugin import Provider, ProviderFailedException

#from collections import OrderedDict
import os
import anymarkup
import subprocess
from distutils.spawn import find_executable

import logging

logger = logging.getLogger(__name__)


class AnsibleProvider(Provider):
    key = "ansible"
    cli_str = "ansible-playbook"
    inventory = "/etc/ansible/hosts"
    params = None

    def init(self):
        self.container = False
        self.cli = find_executable(self.cli_str)
        if self.config.get("provider_cli"):
            self.cli = self.config.get("provider_cli")
        if self.container:
            self.cli = os.path.join("/host", self.cli.lstrip("/"))
        if not self.cli or not os.access(self.cli, os.X_OK):
            raise ProviderFailedException("Command %s not found" % self.cli)
        else:
            logger.debug("Using %s to run commands.", self.cli)

    def deploy(self):
        for artifact in self.artifacts:
            logger.info("Deploying playbook %s" % artifact)
            playbook = os.path.join(self.path, artifact)
            self._callCli(self.inventory, artifact)

    def _callCli(self, inventory, path):
        logger.info(self.config)
        cmd = [self.cli,
               os.path.join(path, self.config['playbook'])]
        if self.config['ansible-opts']:
            cmd.append(" ".join(self.config['ansible-opts'].split()))
        if self.dryrun:
            cmd.append("--list-tasks")
            logger.info("Calling: %s", " ".join(cmd))
        else:
            subprocess.check_call(cmd)

