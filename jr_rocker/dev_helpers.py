import pkgutil

import em

from rocker.extensions import RockerExtension


class DevHelpers(RockerExtension):

    name = 'jr_dev_helpers'

    @classmethod
    def get_name(cls):
        return cls.name

    def __init__(self):
        self._env_subs = None
        self.name = DevHelpers.get_name()

    def get_environment_subs(self):
        if not self._env_subs:
            self._env_subs = {}
        return self._env_subs

    def get_preamble(self, cliargs):
        return ''

    def get_snippet(self, cliargs):
        snippet = pkgutil.get_data(
            'jr_rocker',
            'templates/{}_snippet.Dockerfile.em'.format(self.name)).decode('utf-8')
        return em.expand(snippet, self.get_environment_subs())

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument('--jr-dev-helpers',
                            action='store_true',
                            help='install development tools')
