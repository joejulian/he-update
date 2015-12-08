from setuptools import setup,find_packages
import pip

install_reqs = pip.req.parse_requirements('requirements.txt', 
        session=pip.download.PipSession())

setup(
  name = 'he_update',
  packages = find_packages(),
  version = '1.1',
  description = 'Hurricane Electric tunnel endpoint and dyndns updater',
  author = 'Joe Julian',
  author_email = 'me@joejulian.name',
  url = 'https://github.com/joejulian/he-update', 
  download_url = 'https://github.com/joejulian/he-update/tarball/v1.1', 
  keywords = ['tunnel', 'ipv6', 'dyndns', 'Hurricane','update'],
  classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Environment :: Console',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Programming Language :: Python',
      'Topic :: Internet :: Name Service (DNS)',
      'Topic :: System :: Networking',
      'Topic :: Utilities',
      ],
  install_requires = [str(ir.req) for ir in install_reqs],
  entry_points = {
      'console_scripts': [
          'he-update=he_update:execute',
          ],
      },
)
