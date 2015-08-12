"""
Update the below LABELS if ATOMICAPPVERSION & NULECULESPECVERSION are updated:
1) LABEL io.projectatomic.nulecule.atomicappversion in atomicapp Dockerfile
2) LABEL io.projectatomic.nulecule.specversion  in app Dockefile
"""
__ATOMICAPPVERSION__ = '0.1.1'
__NULECULESPECVERSION__ = '0.0.2'

EXTERNAL_APP_DIR = "external"
GLOBAL_CONF = "general"
APP_ENT_PATH = "application-entity"

PARAMS_KEY = "params"
MAIN_FILE = "Nulecule"
ANSWERS_FILE = "answers.conf"
ANSWERS_FILE_SAMPLE = "answers.conf.sample"
ANSWERS_FILE_SAMPLE_FORMAT = 'ini'
WORKDIR = ".workdir"
LOCK_FILE = "/run/lock/atomicapp.lock"

DEFAULT_PROVIDER = "kubernetes"
DEFAULT_NAMESPACE = "default"
DEFAULT_ANSWERS = {
    "general": {
        "provider": DEFAULT_PROVIDER,
        "namespace": DEFAULT_NAMESPACE
    }
}
